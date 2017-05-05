import traceback

import hues

import settings
from plugin_system import PluginSystem
from settings import PREFIXES
from utils import convert_to_rus, convert_to_en, MessageEventData
from vkplus import Message


class CommandSystem(object):
    def __init__(self, commands, plugin_system: PluginSystem, convert_layout=True):
        # Система плагинов
        self.system = plugin_system
        # self.commands - список с командами
        self.commands = commands
        self.ANY_COMMANDS = bool(plugin_system.any_commands)
        # Конвертировать ли команду в русскую раскладку?
        self.convert = convert_layout

    def check_command(self, cmd):
        if not cmd.has_prefix:
            return False

        # Если команда (обычная или сконвертированная) есть в списке команд
        if cmd.command in self.commands:
            pass

        # Если команды нет в списке команд - можно попробовать перевести
        # её в другую раскладку и проверить, есть ли конвертированная команда
        # в списке команд
        elif self.convert and cmd.try_convert() in self.commands:
            cmd.convert()

        # Если есть плагины, которые срабатывают на любые команды
        elif self.ANY_COMMANDS:
            pass

        # Не обрабатываем сообщение
        else:
            return False

        return True

    async def process_command(self, msg_obj: Message):
        """Обрабатывает команду (объект Message)"""
        cmd = Command(msg_obj._data, self.convert)

        if not self.check_command(cmd):
            if cmd.args:
                cmd.command += ' ' + cmd.args.pop().lower()

                if not self.check_command(cmd):
                    return

            else:
                return

        cmd_text = cmd.command

        # Логгируем команду, если нужно (но не логгируем плагины,
        # которые реагируют на любые команды)
        if settings.LOG_COMMANDS and not self.ANY_COMMANDS:
            cmd.log()
        try:
            await self.system.call_command(cmd_text, msg_obj, cmd.args)
            return True
        # Если в плагине произошла какая-то ошибка
        except Exception:
            await msg_obj.answer(f"{msg_obj.vk.anti_flood()}. "
                                 f"Произошла ошибка при выполнении команды <{cmd_text}> "
                                 "пожалуйста, сообщите об этом разработчику!")
            hues.error(
                f"Произошла ошибка при вызове команды '{cmd_text}' с аргументами {cmd.args}. "
                f"Текст сообщения: '{msg_obj._data}'."
                f"Ошибка:\n{traceback.format_exc()}")


class Command(object):
    __slots__ = ('has_prefix', '_data', 'text',
                 'command', 'args', 'need_convert')

    def __init__(self, data: MessageEventData, convert: bool):
        self.has_prefix = True  # переменная для обозначения, есть ли у команды префикс
        self._data = data
        self.text = data.body
        self.need_convert = convert
        self._get_prefix()
        self.command, *self.args = self.text.split(' ')
        self.command = self.command.lower()
        # Если команда пустая
        if not self.command.strip():
            self.has_prefix = False

    def try_convert(self):
        """Возвращает команду, переведённую в русскую раскладку"""
        return convert_to_rus(self.command)

    def convert(self):
        """Конвертирует команду и все аргументы в русскую раскладку"""
        self.command = convert_to_rus(self.command)
        self.args = [convert_to_rus(arg) for arg in self.args]

    def log(self):
        """Пишет в лог, что была распознана команда"""
        pid = self._data.peer_id
        who = ("конференции {}" if self._data.conf else "ЛС {}").format(pid)
        hues.info(f"Команда '{self.command}' из {who} с аргументами {self.args}")

    def _get_prefix(self):
        """Пытается получить префикс из текста команды"""
        for prefix in PREFIXES:
            # Если команда начинается с префикса
            if self.text.startswith(prefix):
                # Убираем префикс из текста
                self.text = self.text.replace(prefix, '', 1).lstrip()
                break
            elif self.need_convert:
                # Префикс, написанный русскими буквами, но на английской раскладке
                prefix_en = convert_to_en(prefix)
                # Если команда начинается с префикса в английской раскладке
                if self.text.startswith(prefix_en):
                    # Убираем префикс из текста
                    self.text = self.text.replace(prefix_en, '', 1).lstrip()
                    break
        else:
            self.has_prefix = False

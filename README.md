<p align="center">
    <img src="https://github.com/vk-brain/sketal/blob/master/docs/title.png?raw=true" alt="vk-sketal logo"/>
</p>

## sketal

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1a5af7a2447a4f83838cb4ea9da0bb43)](https://www.codacy.com/app/m-krjukov/Sketal?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vk-brain/sketal&amp;utm_campaign=Badge_Grade) [![Build Status](https://travis-ci.org/vk-brain/sketal.svg?branch=master)](https://travis-ci.org/vk-brain/sketal)

#### Немного о боте
- Бот работает на python3.6 и выше. Ниже не работает. Совсем. Это важно.
- Бот использует asyncio, aiohttp и т.д.

#### Инструкция
1. Скачать python версии 3.6 или выше и установить его (с возможностью работать с ним из командной строки)
```
Можно скачать Python3.6 с оф. сайта: https://www.python.org/downloads/
```

2. Установить модули для python с помощью pip (модуля python). Список модулей находится в requirements.txt
```
python -m pip install -r requirements.txt
```

3. Заполнить настройки в settings.py (заменить нужные поля и т.д.).  
   Как минимум необходимо ввести `api ключ сообщества` вконтакте.

4. Бота можно запустить следующим способом из командной строки (windows) или терминала (linux) и т.д.:
   ```
   python bot.py
   ```

#### Как запустить бота от лица пользователя?
```
USERS = (
        ("group", "ТОКЕН СООБЩЕСТВА",),
        ("user", "ЛОГИН ПОЛЬЗОВАТЕЛЯ", "ПАРОЛЬ ПОЛЬЗОВАТЕЛЯ",),
        ("user", "ТОКЕН ПОЛЬЗОВАТЕЛЯ",),
)
```
Пример возможного содержания переменной USERS. Если вам нужно использовать пользователя для бота - замените `("group", "API КЛЮЧ СООБЩЕСТВА",),` на `("user", "ЛОГИН ПОЛЬЗОВАТЕЛЯ", "ПАРОЛЬ ПОЛЬЗОВАТЕЛЯ",),`. Обратите внимание на запятые!

#### Документация
Как таковой документации проект сейчас не имеет. Многие функции, примеры, возможности бота можно найти, изучая исходный код плагинов и файлы бота. Например: `tests.py`, `vk/helpers.py`, `handler/base_plugin.py` и т.д.

#### Материалы:
- [Sketal. Быстрый ввод в разработку плагинов.](https://vk.com/@vkbraindev-quick-dev-start)
- [Как бесплатно захостить Sketal (деплой на Heroku).](http://disonds.com/2018/01/31/razviertyvaniie-python-bota-sketal-dlia-vkontaktie-na-heroku/)

#### Замечания
-  Никакие плагины не должны менять код основных частей бота, чтобы было легко обновляться и менять какие-то базовые вещи (переписывать плагины легче, чем восстанавливать функционал после обновлений).
- При использовании CommandPlugin помните, что команды сортируются в соответствии с количесвом пробелов в команде (от большего к меньшему)
- Многие плагины требуют `PeeweePlugin` (база данных).
- Крайне рекомендуется использовать `AdminPlugin` (контроль привилегий).

#### Участники проекта:
- [Список участников (все молодцы! большие!)](https://github.com/vk-brain/sketal/graphs/contributors)
- [Плагинчик сделал](https://github.com/TumkasCor)
- [Плагинчик сделал](https://github.com/Lis1us)

@michaelkrukov http://michaelkrukov.ru/

Проект command_line

Задание:

Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу
эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.
Эмулятор должен запускаться из реальной командной строки, а файл с
виртуальной файловой системой не нужно распаковывать у пользователя.
Эмулятор принимает образ виртуальной файловой системы в виде файла формата
zip. Эмулятор должен работать в режиме CLI.
Конфигурационный файл имеет формат json и содержит:
• Имя пользователя для показа в приглашении к вводу.
• Путь к архиву виртуальной файловой системы.
• Путь к стартовому скрипту.
Стартовый скрипт служит для начального выполнения заданного списка
команд из файла.
Необходимо поддержать в эмуляторе команды ls, cd и exit, а также
следующие команды:
1. du.
2. wc.
3. chown.
Все функции эмулятора должны быть покрыты тестами, а для каждой из
поддерживаемых команд необходимо написать 3 теста.

Структура файлов в проекте:

system.zip - Архив, с которым мы будем работать, в нём содержится несколько папок и файлов (etc, bin, rights_access.txt ...)
conf.json - Конфигурационный файл, содержит 3 параметра(username , conf_path , script_path)
commands.py - Файл скрипта, в котором мы работаем над созданием команд CLI и их вызовом(ls, cd, du, wc, chown, exit)
emulator.py - Главный файл скрипта, в котором мы выгружаем содержимое архива во временную папку и работаем с ней, а также оперируем вызовом команд с файла commans.py
tests.py - Файл скрипта, в котором мы прописываем тесты для команд и смотрим их правильность выполнения

Описание команд CLI:
ls - просмотр содержимого директорий
cd - переход в другую директорию
du - указывает объём директории/файла
wc - подсчитывает количество строк, слов и байтов в файле
chown - изменяет владельца/группы для файла/директории
exit - прерывание работы эмулятора

Работа с эмулятором : 

![Image alt](https://github.com/sanyochek58/emulator_cli/blob/main/pics/Snimok_ekrana_2024-10-24_000532.png)

![Image alt](https://github.com/sanyochek58/emulator_cli/blob/main/pics/Snimok_ekrana_2024-10-24_025329.png)

![Image alt](https://github.com/sanyochek58/emulator_cli/blob/main/pics/Snimok_ekrana_2024-10-24_031559.png)

![Image alt](https://github.com/sanyochek58/emulator_cli/blob/main/pics/Snimok_ekrana_2024-10-24_031616.png)

![Image alt](https://github.com/sanyochek58/emulator_cli/blob/main/pics/Snimok_ekrana_2024-10-24_031707.png)

![Image alt](https://github.com/sanyochek58/emulator_cli/blob/main/pics/Snimok_ekrana_2024-10-24_031707.png)

![Image alt](https://github.com/sanyochek58/emulator_cli/blob/main/pics/Snimok_ekrana_2024-10-24_031743.png)

![Image alt](https://github.com/sanyochek58/emulator_cli/blob/main/pics/Snimok_ekrana_2024-10-24_031810.png)



# Добро пожаловать в курс по программированию на языке Python!
## Описание курса:
В этом курсе вы узнаете основы языка Python и научитесь программировать на нем.  Так-же мы ознакомимся с фреймворком Django, который позволит вам быстро начать разработку веб-приложений.
### В курсе вы научитесь:
- Программировать на языке Python
- Применять функции Git для управления версиями проекта
- Использовать pipenv для создания и управления виртуальной средой исполнения Python
- Использовать фреймворк Django для создания веб-приложений
- Использовать Docker для управления проектом и его компонентами
- Деплойментировать приложение на сервере AWS или Google Cloud

В процессе изучения языка Python вы будете получать домашние задания и практические задания, которые помогут вам продвинуться в направлении программирования.

#### Offtopic
Вы мой второй класс. 
Мне мой первый клас сказал что я хорошо мотивирую так-что если это будет наше единственное занятие вот мои наставления: Перед тем как пойти во второй раз я сделал опрос старой группы.  

Первый я провёл весна-лето 2021 года и 10 из 13ти студентов работают программистами.  Причём 1го наняли сразу после защиты проекта.  Остальные или нашли работу ходя по интервью или после стажеровки.

2 человека решили что хотят изучать английский в то время как те кто англйского не зная уже работают.  Ещё один человек взял курс для своего развития но работать программистом и не собирался никогда.

Защита это хороший шанс для тех кто ищет работу чтобы найти её сразу по окончанию курса так как есть надобность в питон разрабочиках.

Есть такая тема что с ковидом многие работы в штатах (особенно сектор IT) перешли на удалёнку.  Следующий логический шаг для больших компаний перенести эти работы за океан или обратно в офис.  В офис никто не хочет так-что remote рынок будет увеличиваться.  Это большой плюс для Индии но есть надежда что и Беларусь этот рост не обойдёт стороной.

## Setup
Для начала стоит подготовить наши компьютеры к работе.  Я обычно работаю на макинтоше но думаю в этот раз проделать тоже на виндоусе.  Первое что нам понадобится это то где мы будем писать код.  
### PyCharm
Самым популярным в прошлом году был `PyCharm` у меня о нём двоякое чувство так как это был мой первый питоновский блокнот и он делает нашу работу очень простой но когда я попал на интервью мне пришлось печатать почти от руки и был нейкий шок когда я нажимаю `tab` а за меня ничего не пишется!  Другой минус пайчарма в том что он платный но есть `Community Edition`.  Я буду работать в этом так как всё равно большинство будет работать с пайчармом просто старайтесь не отключять мозги когда работаете в нём.
### VS Code
Визуальная студия от майкрософт тоже очень хорошая IDE (Independent Development Environment) может всё на всех языках но бесплатно! И это большой бонус.
### Atom
Как я за атом не болел и всё ещё им пользуюсь для разработки в php его не полюбили в прошлый раз так-что здесь я его пихать не буду.  На равне с Sublime простой блокнотик с непростыми разширениями типа писать код прямиком на сервере и полностью открыт к модификации.  Весь курс в атоме провёл но он никому не прижился хотя он для меня решил ту проблему с отключением мозга описаную в случае с пайчарм.

https://atom.io/

Я рекомендую первое время пользоваться тем чем я пользуюсь а потом уже искать то что соответствует вашей философии.

https://www.jetbrains.com/pycharm/

## Terminal
Без этого жить можно но я пользуюсь терминалом постоянно и вам рекомендую хотябы по тому что знание `Linux` комманд даст вам галочку над другими программистами.  По сколько мы будем работать в виндоусе даже майкрософт признал что их програмное обеспечение не очень подходит програмистам и чтобы не терять пользователей `Linux` они сделали порт терминала линукса.  Следуем инструкциям по этой ссылке:

https://ubuntu-admin.ru/ubuntu-wsl/

Так-же есть альтернативы для прользователей виндоус это при скачке Git получается неплохой терминал но это лишь имитация оригинала который мы получим с ubuntu. Кто на макинтоше можно пользоваться терминалом но советую испльзовать 'brew' в место 'apt' сами найдёте как это установить там всё предельно просто!

## Python
Python это энтерпритируемый язык что значит чтобы наш код работал на железе его нужно перевести в машинный код.  Для этого мы скачаем переводчик питона здесь:
https://www.python.org/downloads/

Это на самом деле опционально так как наш линукс имеет встроенный питон попробуем команду:
```sh
python3 --version
```
Разберем эту команду:
- `python3` название программы которую мы запускаем
- '--version' комманда этой программе в данном случае хотим увидеть версию сей программы
И мы увидим последнюю стабильную версию питона.  Почему `python3`? Есть долгий рассказ который я расскажу вам но чтобы упростить жизнь мы превратим `python3` в `python` при помощи одной команды:

```sh
sudo apt install python-is-python3
```
Разберем эту команду
- `sudo` программа способная запускать процессы с администраторскими привелегиями так как нам нужно менять системные файлы
- `apt` это линуксный менеджер программ
- `install` команда установить пакет для апта
- `python-is-python3` имя пакета который мы хотим установить

## Git & GitHub
У нас на это ушёл целый урок в прошлый раз хотя система Git заслуживает своего курса я это отложу на 2ую неделю хотя прелести вы отцените только на финальных проектах.  Кто на маке не нужно морочиться гит уже в системе. Кто на линуксе там 50 на 50 зависит от линукса но `apt-get` достанет всё. У кого винда идите по ссылке и скачивайте:

https://git-scm.com/downloads

### GitHub
Всем нужны гитхаб аккаунты это не займёт долго

https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

При помощи Git мы сможем

# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код верстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

### Как установить

- Вы скачаете на компьютер архив с кодом
-  Вы запустите в терминале команду python --version, чтобы убедиться что установлена третья версия Python не младше 3.5.0
- Также вы убедитесь, что установлен pip, запустив его в командной строке. Номер версии pip не имеет значения.
- Установите django версии 3.2
- запустите сайт на вашем пк через команду в терминале python manage.py runserver 0.0.0.0:8000
### Виртуальное окружение 
###### Виртуальное окружение — это изолированная среда, позволяющая устанавливать и использовать пакеты Python отдельно от глобальной установки. В файле settings.py находится переменные настройки окружения например словарь DATABASES, DEBUG, SECRET_KEY, ALLOWES_HOSTS их вы можете поменять под себя для ваших целей.
- Переменная DATABASES - основная информация такие как порт, хостинг, пользователь, название
- Переменная DEBUG - настройка отладки сайта в ней работают настройки TRUE,True,true для включения отладки, и FALSE, False, false для отключения отладки.
- Переменная SECRET_KEY - секретный ключ уже по названию понятно что он очень секретный сделайте свой секретны ключ что бы использовать этот код.

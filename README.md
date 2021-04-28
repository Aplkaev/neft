# neft
Контрольное задание от "Роснефть"
____
Для загрузки файлов с клиента использовался [dropzone](https://www.dropzonejs.com/)
____
db - mysql
Перед настройкой mysql надо установить ```pip install mysqlclient```

Настройка db в [settigs.py](https://github.com/Aplkaev/neft/blob/main/bash/bash/settings.py) 
```
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bash',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
____
[xampp-windows-x64-7.4.16-0-VC15](https://sourceforge.net/projects/xampp/files/XAMPP%20Windows/7.4.16/)
MariaDB 10.4.18

Конфигурация из коробки
____
Разместить проект можно, где будет удобно вам запускать ```python manage.py runserver```


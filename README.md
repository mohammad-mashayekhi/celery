 # نصب celery در جنگو
ر این پروژه مثال عملی از عملکر celery و وظایف زمان‌بندی شده در جنگو خواهیم دید.
ابتدا به توضیخی در مورد celery و نحوه نصب آن می‌پردازیم و سپس به با redis آن را راه اندازی می‌کنیم.
در انتها با تعریف چند تابع به بررسی عملکرد آن می‌پردازیم.

## فهرست مطالب (Table of Contents)

1. [نصب و راه‌اندازی](#installation)
2. [مثال استفاده](#usage)
3. [مشارکت](#contributing)
4. [مجوز](#license)
5. [اطلاعات تماس](#contact)

## نصب و راه‌اندازی (Installation)

بعدز از ساخت پروژه در جنگو به نصب celery بپردازید.
برای نصب و راه‌اندازی celery، مراحل زیر را دنبال کنید:

نصب redis در windows
```sh
https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/
```
نصب redis در linox
```sh
https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/
```
نصب redis در macos
```sh
https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-mac-os/
```
به صورت کلی با دستور ترمینال به راحتی می‌توانید redis را در دستگاه خود نصب کنید. پس از آن با دستور redis-server می‌توانید مشخصات اولیه redis را ببینید.
![image](https://github.com/user-attachments/assets/c83704c4-81bb-41cb-ba0e-3476297ab9cc)
همچنین با دستور زیر می‌توانید از نصب درست redis مطمین شوید
```sh
redis-cli
```
![image](https://github.com/user-attachments/assets/630fb96e-4725-4250-babf-f7384ad0e16c)

نصب celery
```sh
pip install celery
```
راه اندازی worker
```sh
celery -A config worker -l info
```
همچنین در فایل celery.py در روت اصلی پروژه کانفیگ celery را انجام میدیم:‌
```sh
from celery import Celery
import os

os.environ.setdefault('DLANGO_SETTING_MODULE','config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.beat_schedule = {
    'mytask_every_2min':{
        'task':'home.tasks.mytask2',
        'schedule':2,
        'options':{
            'expires':10,
        }
    }
}
```
و داخل تنظیمات پروژه مقادیر اولیه celery را مشخص می‌کنیم:
```sh
# Celery Configuration Options
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_DEFAULT_QUEUE = 'default'
```

در صورت علاقه‌مندی می‌توان از کتابخانه‌های زیر برای مدیریت بهتر تسک‌ها استفاده کرد 
```sh
pip install django-celery-beat==1.0.0
pip install django-celery-results
```

##  مثال استفاده (usage)
به منظور درگ بهتر، یک تابع مینویسیم که بعد از ده ثانیه فایلی را ایجاد می‌کند. همانطور که بعد از اجرا پروژه می‌بینیم بدون استفاده از celery بارگذاری کامل صفحه وب ۱۰ ثانیه طول می‌کشه اما در صورت از celery وظضیفه به صورت زمان بندی شده انجام میشه و صفحه در کسری از ثانیه هم بارگداری کامل می‌شود.
تابع مورد نظر:
```sh
@app.task
def mytask():
    time.sleep(10)
    open('namefile.txt' , 'w').close
```


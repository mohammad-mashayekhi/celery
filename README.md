 # نصب celery در جنگو
ر این پروژه مثال عملی از عملکر celery و وظایف زمان‌بندی شده در جنگو خواهیم دید.
ابتدا به توضیخی در مورد celery و نحوه نصب آن می‌پردازیم و سپس به با redis آن را راه اندازی می‌کنیم.
در انتها با تعریف چند تابع به بررسی عملکرد آن می‌پردازیم.

## فهرست مطالب (Table of Contents)

1. [نصب و راه‌اندازی](#installation)
2. [نحوه استفاده](#usage)
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



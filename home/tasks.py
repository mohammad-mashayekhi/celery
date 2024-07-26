from celery import shared_task

@shared_task
def mytask2():
    file = open('task.txt','a')
    file.write('hello')
    file.close
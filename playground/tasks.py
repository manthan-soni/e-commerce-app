from time import sleep
# from storefront.celery import celery
from celery import shared_task


# @celery.task
@shared_task
def notify_customers(message):
    print('Sending 10k email...')
    print(message)
    sleep(10)
    print("Successfullt sent")
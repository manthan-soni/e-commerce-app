from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import requests
import logging

# from .tasks import notify_customers
# from django.core.mail import EmailMessage, BadHeaderError
# from templated_mail.mail import BaseEmailMessage

# def say_hello(request):
#     # try:
#         # send_mail('subject', 'message', 'from@ms.com', ['manthan04soni@gmail.com'])
#         # mail_admins('subject', 'message', html_message='message')
#         # message = EmailMessage('subject', 'message', 'from@ms.com', ['manthan04soni@gmail.com'])
#         # message.attach_file('playground/static/images/course-1.jpg')
#         # message.send()
#     #     message = BaseEmailMessage(
#     #         template_name='emails/hello.html',
#     #         context={'name':'Mosh'}
#     #     )
#     #     message.send(['manthan04soni@gmail.com'])
#     # except BadHeaderError:
#     #     pass
#     # notify_customers.delay('Hello')
#     key = 'httpbin_result'
#     if cache.get(key) is None:
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()
#         cache.set(key, data)
#         # cache.set(key, data, 10*60)
#     return render(request, 'hello.html', {'name': cache.get(key)}) 


# @cache_page(5*60)
# def say_hello(request):
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, 'hello.html', {'name': data}) 


# class HelloView(APIView):
#     @method_decorator(cache_page(5*60))
#     def get(self, request):
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()
#         return render(request, 'hello.html', {'name': data})     

logger = logging.getLogger(__name__) 

class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbib')
            response = requests.get('https://httpbin.org/delay/2')  
            logger.info('Recieved the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': data})     

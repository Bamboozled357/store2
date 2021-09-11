from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Product

# Создать продукты в БД через админку и сделать View для листинга продуктов по адресу products/
# Залить проект в гитхаб

def view(request):
    products = Product.objects.all()
    return HttpResponse(products)




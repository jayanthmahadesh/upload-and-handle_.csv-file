from datetime import datetime
from django.shortcuts import render,redirect
from .models import File,sales
import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import sales_serializer
# Create your views here.
def create_database(filepath):
    df = pd.read_csv(filepath,delimiter=',')
    sales_list = [list(rows) for rows in df.values]
    c=0
    for iterator in sales_list:
        if(c>=60):
            break
        date_obj = datetime.strptime(str(iterator[10]), '%m/%d/%Y').date()
        time_obj = datetime.strptime(str(iterator[11]), '%H:%M').time()
        sales.objects.create(
            invoice_id = iterator[0],
            product_line = iterator[5],
            unit_price = iterator[6],
            quantity = iterator[7],
            tax = iterator[8],
            total = iterator[9],
            date = date_obj,
            time=time_obj,
        )
        c=c+1
def homepage(request):
    if request.method=="POST":
        file = request.FILES['file']
        path = File.objects.create(file=file)
        # print("path = "+str(path.file))
        if str(path.file).endswith(".csv"):
            create_database(path.file)
        else:
            print('file is not of type .csv')
    return render(request,'homepage.html')
class custom(APIView):
    def get(self,request):
        data = sales.objects.all()
        data = data.filter(product_line='Health and beauty')
        try:
            serializer = sales_serializer(data,many=True)
        except:
            print("inside except")
        # return Response({'satus':200 , 'payload':serializer.data})
        return render(request,'display.html',{'datas':serializer.data})

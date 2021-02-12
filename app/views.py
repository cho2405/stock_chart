from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
from app.models import KospiPredict
from time import mktime, strptime

class KospiPredictAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        stocks = KospiPredict.objects.all().order_by('date')

        close_list = []
        open_list = []
        for stock in stocks:
            time_tuple = strptime(str(stock.date), '%Y-%m-%d')  
            utc_now = mktime(time_tuple) * 1000           
            close_list.append([utc_now, stock.close])
            open_list.append([utc_now, stock.open])

        data = {
            'close': close_list,
            'open': open_list
        }

        return Response(data)

class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/chart.html')


def index(request):
	return HttpResponse('Hi')


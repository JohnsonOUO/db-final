from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from home.models import *
from django.urls import reverse
from twstock import BestFourPoint
import requests
#import yfinance as yf
import random
import json
import time
import twstock 
#更新 TPEX 跟 TWSE 的列表
from twstock import Stock
twstock.__update_codes()
# Create your views here.
requests.adapters.DEFAULT_RETRIES = 10
s = requests.session()
s.keep_alive = False
# s.get('http://www.twse.com.tw')
def search(request):
    if request.method == "POST":
        # try:
        query_info = request.POST
        query = query_info['num']
        if query is not None:
            try:
                a = int(query)
            except:
                return HttpResponseRedirect(reverse('home'))
            if(a > 9999 or a < 1000):
                return HttpResponseRedirect(reverse('home'))
            print(query)
            try:
                test1 = stock_info.objects.get(stock_id=query)
            except:
                return HttpResponseRedirect(reverse('home'))
            template = loader.get_template('stockInfo.html')
            print("work")
            context = {
                'tests1': test1,
            }
            var = '/stockInfo/'+query
            print(var)
            print(type(var))
            #url = reverse('stockInfo', kwargs={'num': query})#args=(str(self.id),)
            url = reverse('stockInfo', args=(str(query),))
            return HttpResponseRedirect(url)
                #return HttpResponse(template.render(context, request))
        # except Exception:
        #         print("Error")
        #         pass
        
def stockInfo(request, num):
    #test1 = Test.objects.get(num=num)
    #stock = Stock(num)
    #stock_price = Stock(num).price
    #cost = (stock_price.price)[-1]
    stockdetails = twstock.codes[num]
    time.sleep(2)
    stockrealtime = twstock.realtime.get(num)
    time.sleep(2)
    bfp = BestFourPoint(Stock(num)) 
    Buy = bfp.best_four_point_to_buy()
    Buy1 = bfp.best_buy_1()
    Buy2 = bfp.best_buy_2()
    Buy3 = bfp.best_buy_3()
    Buy4 = bfp.best_buy_4()
    Sell = bfp.best_four_point_to_sell()
    Sell1 = bfp.best_sell_1()
    Sell2 = bfp.best_sell_1()
    Sell3 = bfp.best_sell_1()
    Sell4 = bfp.best_sell_1()
    Result = bfp.best_four_point()
    template = loader.get_template('stockInfo.html')
    context = {
        #'tests1': test1,
        'stockdetails': stockdetails,
        'stockrealtime': stockrealtime,
        'buy': Buy,
        'buy1': Buy1,
        'buy2': Buy2,
        'buy3': Buy3,
        'buy4': Buy4,
        'sell': Sell,
        'sell1': Sell1,
        'sell2': Sell2,
        'sell3': Sell3,
        'sell4': Sell4,
        'result': Result,
        # 'cost': stock_price,
        # 'stock': stock,
    }
    return HttpResponse(template.render(context, request))
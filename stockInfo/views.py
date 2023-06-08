from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from home.models import Test
from twstock import BestFourPoint
#import yfinance as yf
import random
import json

import twstock 
#更新 TPEX 跟 TWSE 的列表
from twstock import Stock
twstock.__update_codes()
# Create your views here.
def search(request):
    if request.method == "POST":
        try:
            query_info = request.POST
            query = query_info['num']
            if query is not None:
                print(query)
                test1 = Test.objects.get(num=query)
                template = loader.get_template('stockInfo.html')
                print("work")
                context = {
                    'tests1': test1,
                }
                return HttpResponse(template.render(context, request))
        except Exception:
                pass
        
def stockInfo(request, num):
    test1 = Test.objects.get(num=num)
    stockdetails = twstock.codes[num]
    stockrealtime = twstock.realtime.get(num)
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
        'tests1': test1,
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
    }
    return HttpResponse(template.render(context, request))
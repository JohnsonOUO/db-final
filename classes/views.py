from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
# import twstock 
# twstock.__update_codes()
# from twstock import Stock

import pandas as pd
from home.models import *

List_traditon = ['航運業', '鋼鐵工業', '電機機械', '電器電纜', '汽車工業', '化學工業', '油電燃氣業', '生技醫療業', '建材營造業', \
                 '水泥工業','食品工業','塑膠工業','紡織纖維','貿易百貨業','玻璃陶瓷','造紙工業','橡膠工業','觀光事業','其他業']

# def classes(request):
#     #stock = Stock('2885')
#     template = loader.get_template('classes.html')
#     return HttpResponse(template.render())

# def stock_industry(request):
#     df = pd.read_csv("D:/學校/111學年/資料庫/專題/db-final/classes/NewTotalCompany.csv")
#     num_of_stocks = df["product"] == '半導體業'
#     result_csv = df[num_of_stocks]["Num"]
#     result = []
#     for i in result_csv:
#         result.append(i)
#     template = loader.get_template('classes.html')
#     context = {
#         'num_of_stocks': result_csv,
#     }
#     return HttpResponse(template.render(context, request))


def stock_industry_search(request, name):
    #df = pd.read_csv("D:/學校/111學年/資料庫/專題/db-final/classes/NewTotalCompany.csv")
    if(name == '傳統產業'):
        df = pd.read_csv("classes/NewTotalCompany.csv")
        result = []
        k = 0
        for m in range(len(List_traditon)):
            num_of_stocks = df["product"] == List_traditon[m]
            for i in df[num_of_stocks]["Num"]:
                result.append([i])
            for j in df[num_of_stocks]["Name"]:
                result[k].append(j)
                k += 1
        template = loader.get_template('classes.html')
        context = {
            'num_of_stocks': result,
            'product_name': name,
        }
    else:
        df = pd.read_csv("classes/NewTotalCompany.csv")
        num_of_stocks = df["product"] == name
        

        #單純股票代碼
        result_csv = df[num_of_stocks]["Num"]

        #股票代碼+公司名稱
        result = []
        for i in df[num_of_stocks]["Num"]:
            result.append([i])
        k = 0
        for j in df[num_of_stocks]["Name"]:
            result[k].append(j)
            k += 1
        template = loader.get_template('classes.html')
        context = {
            'num_of_stocks': result,
            'product_name': name,
        }

    return HttpResponse(template.render(context, request))




from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
# import twstock 
# twstock.__update_codes()
# from twstock import Stock

import pandas as pd

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




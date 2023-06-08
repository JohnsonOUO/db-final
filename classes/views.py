# from django.shortcuts import render
# from django.http import HttpResponse 
# from django.template import loader
# import twstock 
# twstock.__update_codes()
# from twstock import Stock

# stock = Stock('2885')                             # 擷取元大股價
# # ma_p = stock.moving_average(stock.price, 5)       # 計算五日均價
# # ma_c = stock.moving_average(stock.capacity, 5)    # 計算五日均量
# # ma_p_cont = stock.continuous(ma_p)                # 計算五日均價持續天數
# # ma_br = stock.ma_bias_ratio(5, 10)                # 計算五日、十日乖離值
# def classes(request):
#     #stock = Stock('2885')
#     template = loader.get_template('classes.html')
#     return HttpResponse(template.render())
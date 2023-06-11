from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Test, Favorite, stock_info

def home(request):
    #查詢功能顯示
    # if request.method == "POST":
    #     print(request.POST['num'])
    #     stock_num = request.POST['num']
    #     stock_info = Stock('stock_num')  
    ##     stock_info = yf.Ticker(stock_num + '.TW')
    ##    name = stock_info.info['symbol']
    ##    cost = stock_info.info["currentPrice"]
    #     name = stock_info.sid
    #     cost = (stock_info.price)[-1]
    #     print(name,cost)
    #     single = Test(num=name,cost=cost)
    #     single.save()
    #     test1 = Test.objects.get(num=name)
    #     template = loader.get_template('stockInfo.html')
    #     context = {
    #         'tests1': test1,
    #     }
    #     return HttpResponse(template.render(context, request))
    tests = Test.objects.all().values()
    testf = Favorite.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'tests': tests,
        'testf': testf,
    }
    # print(request.session['u_name'])
    return HttpResponse(template.render(context, request))
# def stockInfo(request, num):
#     test1 = Test.objects.get(num=num)
#     template = loader.get_template('stockInfo.html')
#     context = {
#         'tests1': test1,
#     }
#     return HttpResponse(template.render(context, request))

def delete(request, stock_id): #1
  Favorited = Favorite.objects.get(stock_id=stock_id) #2
  Favorited.delete() #3
  return HttpResponseRedirect(reverse('home')) #4

def add(request, user_id, stock_id):
  AddFavorite = Favorite(user_id=user_id, stock_id=stock_id)
  AddFavorite.save()
  return HttpResponseRedirect(reverse('home'))
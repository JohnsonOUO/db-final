from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Test, Favorite, stock_info
from login.models import User

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
    if 'u_id' in request.session and request.session['u_id'] > 0:
       #有帳號
       favor_list=[]
       template = loader.get_template('home_login.html')
       user_name =  request.session['u_name']
       user_id = request.session['u_id']
       #user = User.objects.get(user_id=user_id)
       favor = Favorite.objects.filter(user_id_id = user_id)
       for data in favor:
          stock = stock_info.objects.get(stock_id=data.stock_id_id)
          # print(stock.stock_id, stock.stock_name)
          favor_list.append(stock)
       context = {
            'favor': favor_list,
            'username': user_name,
        }
    else:
       #沒帳號
       template = loader.get_template('home.html')
       context = {
        }
    # print(request.session['u_id'])
    return HttpResponse(template.render(context, request))
# def stockInfo(request, num):
#     test1 = Test.objects.get(num=num)
#     template = loader.get_template('stockInfo.html')
#     context = {
#         'tests1': test1,
#     }
#     return HttpResponse(template.render(context, request))

def delete(request, stock_id): #1
  if 'u_id' in request.session and request.session['u_id'] > 0:
    if Favorite.objects.filter(user_id = request.session['u_id'], stock_id = stock_id).exists() == True:
      Favorited = Favorite.objects.get(user_id = request.session['u_id'], stock_id=stock_id) #2
      Favorited.delete() #3
  return HttpResponseRedirect(reverse('home')) #4

def add(request,stock_id):
  if 'u_id' in request.session and request.session['u_id'] > 0:
    print(request.session['u_id'])
    print(stock_id)
    if Favorite.objects.filter(user_id_id = request.session['u_id'], stock_id_id = stock_id).exists() == False:
      print("加入")
      AddFavorite = Favorite(user_id=User.objects.get(user_id=request.session['u_id']), stock_id=stock_info.objects.get(stock_id=stock_id))
      AddFavorite.save()
    return HttpResponseRedirect(reverse('home'))
  else:
    return HttpResponseRedirect(reverse('home'))
  
def favor_class(request, stock_classname):
  print("stock")
  return HttpResponseRedirect(reverse('home'))

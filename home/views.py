from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Test, Favorite, stock_info
from login.models import User

List_traditon = ['航運業', '鋼鐵工業', '電機機械', '電器電纜', '汽車工業', '化學工業', '油電燃氣業', '生技醫療業', '建材營造業', \
                 '水泥工業','食品工業','塑膠工業','紡織纖維','貿易百貨業','玻璃陶瓷','造紙工業','橡膠工業','觀光事業','其他業']

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
      industry = str(request.session['classes'])
      if(industry == '全部'):
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
      elif(industry == '傳統產業'):
        favor_list=[]
        template = loader.get_template('home_login.html')
        user_name =  request.session['u_name']
        user_id = request.session['u_id']
        #user = User.objects.get(user_id=user_id)
        favor = Favorite.objects.filter(user_id_id = user_id)
        for data in favor:
            if(data.stock_id.industry in List_traditon):
              favor_list.append(data.stock_id)
            # print(stock.stock_id, stock.stock_name)
        context = {
              'favor': favor_list,
              'username': user_name,
        }
      else:
        favor_list=[]
        template = loader.get_template('home_login.html')
        user_name =  request.session['u_name']
        user_id = request.session['u_id']
        #user = User.objects.get(user_id=user_id)
        favor = Favorite.objects.filter(user_id_id = user_id)
        for data in favor:
            if(data.stock_id.industry == industry):
              favor_list.append(data.stock_id)
            # print(stock.stock_id, stock.stock_name)
        context = {
              'favor': favor_list,
              'username': user_name,
        }
    else:
       #沒帳號
       request.session['classes'] = "全部"
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
  #print("stock")
  request.session['classes'] = stock_classname
  return HttpResponseRedirect(reverse('home'))

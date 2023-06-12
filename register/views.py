from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import auth
from login.models import User
from home.models import Favorite

# Create your views here.
def register(request):
    if request.method== "POST":
        try:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = User.objects.filter(username=username)
            #print(user.count()==0) # Test
            #已被註冊
            if user.count()!=0:
                print('此帳號被使用')
                message='不可使用此 username = '+username
                template = loader.get_template('register.html')
                context = {
                    'message': message,
                }
                return HttpResponse(template.render(context, request))
            #可使用該帳號註冊
            else:
                #print(user[0].password)
                temp = User(username=username,password=password)
                temp.save()
                favor = Favorite(user_id=temp.user_id, stock_id='2330')
                favor.save()
                message='註冊成功 可由下方登入 !'
                template = loader.get_template('register.html')
                context = {
                    'message': message,
                }
                return HttpResponse(template.render(context, request))
        except IndexError:
            pass
    else:
        request.session['u_id'] = -1
        template = loader.get_template('register.html')
        context = {
        }
        return HttpResponse(template.render(context, request))
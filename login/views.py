from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import auth
from .models import User

# Create your views here.
def login(request):
    if request.method== "POST":
        try:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = User.objects.filter(username=username)
            #print(user.count()==0) # Test
            #未註冊
            if user.count()==0:
                print('No user')
                message='Can not find username = '+username
                template = loader.get_template('login.html')
                context = {
                    'message': message,
                }
                return HttpResponse(template.render(context, request))
            #有註冊
            else:
                print(user[0].password)
                if user[0].password==password:
                    request.session['u_name']=user[0].username
                    print(request.session['u_name'])
                    return HttpResponseRedirect(reverse('home'))
                else:
                    message='Your password is incorrect !'
                    template = loader.get_template('login.html')
                    context = {
                        'message': message,
                    }
                    return HttpResponse(template.render(context, request))
        except IndexError:
            pass
    else:
        request.session['u_id'] = -1
        template = loader.get_template('login.html')
        context = {
        }
        return HttpResponse(template.render(context, request))
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Toilet
from django.contrib.auth.models import User
# from django.http import HttpResponse


def index(request):
    if 'twitter_state' not in request.session or \
       '_auth_user_id' not in request.session or \
       'twitterunauthorized_token_name' not in request.session or \
       '_auth_user_backend' not in request.session or \
       '_auth_user_hash' not in request.session or \
       'social_auth_last_login_backend' not in request.session:
        return redirect('/session/login')

    session_user = User.objects.get(id=request.session.get('_auth_user_id'))
    session_user.backend = 'toilet.modules.auth_manager.PasswordLessAuthBackend'

    login_user = authenticate(username=session_user.username)

    if login_user is not None:
        if login_user.is_active:
            login(request, login_user)

            return redirect('toilet:toilets')
        else:
            return render(request, 'login.html', status=401, context={'failure': 'not_active'})
    else:
        return render(request, 'login.html', status=401, context={'failure': 'not_user'})


def toilets(request):
    toilets = Toilet.objects.all()
    return render(request, 'toilet/index.html', {'toilets': toilets})


def register(request):
    if request.method == 'POST':
        toilet = Toilet()
        toilet.place = request.POST['place']
        toilet.comment = request.POST['comment']
        toilet.latitude = request.POST['latitude']
        toilet.longitude = request.POST['longitude']
        toilet.level = request.POST['level']
        toilet.user = request.user
        toilet.save()
        return redirect('toilet:index')
    else:
        if request.user.is_authenticated():
            return render(request, 'toilet/register.html')
        else:
            return render(request, 'toilet/register.html', {'message': 'not_user'})


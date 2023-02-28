"""palindrome_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from game_api.views import start_game, get_board, update_board, list_games,create_user, delete_user,update_user,user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/create', create_user),
    path('users/delete', delete_user),
    path('users/update', update_user),
    path('users/login', user_login),
    path('games/start', start_game),
    path('games/getboard', get_board),
    path('games/updateboard', update_board),
    path('games/list', list_games)
]
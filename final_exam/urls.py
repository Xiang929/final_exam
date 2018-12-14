"""final_exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from weibo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('sign_in', views.sign_in),
    path('sign_up', views.sign_up),
    path('entrance', views.landing_view),
    path('profile', views.profile_view),
    path('logout', views.logout_view),
    path('users/my', views.MyProfile.as_view()),
    path('users/search', views.UserSearch.as_view()),
    path('posts/all', views.PostList.as_view()),
    path('posts/add', views.PostAdd.as_view()),
    path('posts/delete', views.PostDelete.as_view()),
    path('posts/search', views.PostSearch.as_view()),
    path('posts/<str:name>', views.PostUser.as_view()),
    path('<str:username>/followers', views.FollowerList.as_view()),
    path('<str:username>/following', views.FollowingList.as_view()),
    path('following/add', views.FollowingAdd.as_view()),
    path('following/cancel', views.FollowingCancel.as_view()),
    path('comments/all', views.CommentList.as_view()),
    path('comments/add', views.CommentAdd.as_view()),
    path('comments/delete', views.CommentDelete.as_view()),
    path('liked', views.PostLiked.as_view())
]

"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mysite import views
from django.contrib import admin
from django.urls import path, include
from mysite.views import PracticeView, BlogListView, BlogDetailView
from mysite.views import BlogCreateView, BlogUpdateView, BlogDeleteView, SignUpView
from mysite.views import ArticleListView, ArticleDeleteView, ArticleDetailView, ArticleUpdateView, ArticleCreateView
from mysite.views import SerchResultsListView
# from .views import Article

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fanpage),
    path('hello/', views.hello, name="hello"),
    path('Practice/', PracticeView.as_view(), name="Practice"),
    path('Blog/', BlogListView.as_view(), name="Blog"),
    path('Blog_post/<int:pk>/', BlogDetailView.as_view(), name="post_detail"),
    path('Blog_create/', BlogCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name="post_edit"),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name="post_delete"),
    # 兩個有關登入登出的view
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    # 下方都是有關Article的path
    path('articles/list/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:pk>/edit', ArticleUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete',
         ArticleDeleteView.as_view(), name='article_delete'),
    path('articles/create', ArticleCreateView.as_view(), name='article_create'),
    path('search/', SerchResultsListView.as_view(), name='search_results'),

]

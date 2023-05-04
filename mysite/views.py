from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from mysite.models import Practice, Post, Article
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from django.views import View

# Create your views here.


def fanpage(request):
    return render(request, 'fanpage.html', locals())


def hello(request):
    return render(request, 'hello.html', locals())


class PracticeView(ListView):
    model = Practice
    template_name = "Practice.html"
    context_object_name = "Practices"


class BlogListView(ListView):
    model = Post
    template_name = "blog.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]
    success_url = "/Blog/"


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
    success_url = "/Blog/"


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = "/Blog/"


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class BlogCheckauthor(DetailView):
    pass


# 下方都是有關Article的相關設定 List, detail, update, delete
class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"

# 有關Comment


class CommentGet(DetailView):  # 取得所有comment
    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm  # FormView需要這行來找到確定的FORM名稱
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # grab articl pk
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)  # 還沒跟object對，先False
        comment.article = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})


# Comment結束


class ArticleDetailView(LoginRequiredMixin, DetailView):
    # Article delta view變成一個大的view，內含post 跟Get，因為上面分別model都有定義就不再引述
    # model =Article
    # template_name="article_detail.html"
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_create.html"
    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SerchResultsListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'search_results.html'

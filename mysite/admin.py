from django.contrib import admin
from mysite import models
from django.contrib.auth.admin import UserAdmin
#from .forms import CustomUserCreationForm, CustomUserChangeForm
#from .models import CustomUser
from django.conf import settings
#from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# Register your models here.
    
#class PostsOrder(admin.ModelAdmin):
#    list_display=('title', 'author')
#    ordering=('title')


class CommentInline(admin.TabularInline):
    model = models.Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines=[
        CommentInline,
    ]

#class CommentInline(admin.StackedInline):
 #   model = Comment
 #   extra = 0


'''class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)


admin.site.register(CustomUser, CustomUserAdmin)'''
admin.site.register(models.Practice)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Article, ArticleAdmin)

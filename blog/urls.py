from django.urls import path
from . import views

urlpatterns =[
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/',views.post_new, name='post_new'),
    #path('drafts/', views.post_draft_list, name='post_draft_list'),
    #path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
#<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
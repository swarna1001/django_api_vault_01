from . import views
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('/blogs', views.BlogList.as_view()),
    #path(r'^$', views.article_list, name="list"),
    #path('(?P<slug>[\w-]+)/', views.article_detail, name="detail"),
]

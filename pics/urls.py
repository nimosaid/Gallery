from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.pics_of_day,name='picsToday'),
    url(r'^search/', views.search_results, name='search_results')
]
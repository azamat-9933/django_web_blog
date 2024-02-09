from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/',
         category_page_view, name='category'),
    path('about_us/', about_us_page_view, name='about_us'),
    path('our_team/', our_team_page_view, name='our_team'),
    path('services/', services_page_view, name='services'),
    path('article/<int:article_id>/',
         article_detail_page_view,
         name='article_detail')
]
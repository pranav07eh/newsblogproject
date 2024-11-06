from django.urls import path
from . import views

urlpatterns = [
   path('', views.index,name='index'),
   path('about', views.about),
   path('addnews',views.addnews),
   path('newsdetails/<id>',views.newsdetails,name='newsdetails'),
   path('contact',views.contact),
   path('update_blog/<int:pk>/', views.BlogUpdateView.as_view(), name='update_blog'),
   path('delete_blog/<int:pk>/', views.BlogDeleteView.as_view(), name='delete_blog'), 
]


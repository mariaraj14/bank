from.import views
from django.urls import path
app_name='bank'
urlpatterns = [

    path('',views.demo,name='demo'),
    ]
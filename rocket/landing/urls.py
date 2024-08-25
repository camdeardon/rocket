from django.urls import path
from .views import landing_page,learn_more,login

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('learn-more', learn_more, name='learn_more'),
    path('login', login, name='login'),

]
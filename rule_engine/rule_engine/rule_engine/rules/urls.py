from django.urls import path
from .views import create_rule, evaluate_rule

urlpatterns = [
    path('create_rule/', create_rule, name='create_rule'),
    path('evaluate_rule/', evaluate_rule, name='evaluate_rule'),
]

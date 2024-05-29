from django.urls import path
from pages.views import AboutPageView, RulesPageView

from . import views

app_name = 'pages'

urlpatterns = [
    # path('about/', views.about, name='about'),
    path('', AboutPageView.as_view(), name='about'),
    path('', RulesPageView.as_view(), name='rules'),
    # path('rules/', views.rules, name='rules')
]

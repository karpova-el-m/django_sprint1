# from django.shortcuts import render
from django.views.generic.base import TemplateView


class AboutPageView(TemplateView):

    template_name = 'pages/about.html'

class RulesPageView(TemplateView):

    template_name = 'pages/rules.html'

# def about(request):
#     return render(request, 'pages/about.html')


# def rules(request):
#     return render(request, 'pages/rules.html')

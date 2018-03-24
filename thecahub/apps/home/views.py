from django.shortcuts import render

from django.views.generic import TemplateView

class HomeView(TemplateView):
    """
    Home Page
    """
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


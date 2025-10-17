from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AboutSection
from .forms import AboutSectionForm

# Create your views here.


class AboutList(generic.ListView):

    queryset = (
        AboutSection.objects
        .exclude(section_name__icontains="exhibition")
        .order_by('pk')
    )
    template_name = "about/about.html"
    context_object_name = 'about_list'


class ExhibitionList(generic.ListView):

    queryset = (
        AboutSection.objects
        .filter(section_name__icontains="exhibition")
        .order_by('pk')
    )
    template_name = "about/exhibitions.html"
    context_object_name = 'exhibition_list'

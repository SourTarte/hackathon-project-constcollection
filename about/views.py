from django.views import generic
from .models import AboutSection

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

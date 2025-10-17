from django.views import generic
from django.shortcuts import render, redirect
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


def about_create(request):
    """Function view to create a new AboutSection via front-end form."""
    if request.method == 'POST':
        form = AboutSectionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = AboutSectionForm()

    return render(request, 'about/about_form.html', {'form': form})
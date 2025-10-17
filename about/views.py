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


@login_required
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


@login_required
def about_edit(request, pk):
    """Edit an existing AboutSection."""
    section = get_object_or_404(AboutSection, pk=pk)

    if request.method == 'POST':
        form = AboutSectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = AboutSectionForm(instance=section)

    return render(
        request,
        'about/about_form.html',  # change to admin panel
        {'form': form, 'section': section},
    )


@login_required
def about_delete(request, pk):
    """Confirm and delete an AboutSection."""
    section = get_object_or_404(AboutSection, pk=pk)
    if request.method == 'POST':
        section.delete()
        return redirect('about')
    return render(
        request,
        'about/about_confirm_delete.html',  # modal and admin panel instead
        {'section': section},
    )
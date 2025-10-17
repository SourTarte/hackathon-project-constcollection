from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Category, Media
from .forms import CategoryForm, MediaForm
from about.forms import AboutSectionForm
from about.models import AboutSection


def welcome_view(request):
    return render(request, 'gallery/welcome.html')


def art_view(request):
    # Prefetch all media for each category, ordered by created_on
    categories = Category.objects.all().order_by('list_position').prefetch_related('media')
    return render(request, 'gallery/art.html', {'categories': categories})


def category_delete(request, category_id):
    print(request.META.get('HTTP_REFERER'))
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    print(f"Button clicked for {category_id}")
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def media_delete(request, media_id):
    print(request.META.get('HTTP_REFERER'))
    media = get_object_or_404(Media, id=media_id)
    media.delete()
    print(f"Button clicked for {media_id}")
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def admin_view(request):
    # instantiate other forms so template can always render them
    category_form = CategoryForm()
    media_form = MediaForm()
    about_form = AboutSectionForm()

    # If GET includes edit param, prefill the about form with that instance
    edit_pk = request.GET.get('edit')
    if edit_pk:
        section = get_object_or_404(AboutSection, pk=edit_pk)
        about_form = AboutSectionForm(instance=section)

    if request.method == "POST":
        category_form = CategoryForm(data=request.POST)
        media_form = MediaForm(data=request.POST, files=request.FILES)
        form_type = request.POST.get('form_type')

        if form_type == 'about':
            about_pk = request.POST.get('about_pk')
            if about_pk:
                section = get_object_or_404(AboutSection, pk=about_pk)
                about_form = AboutSectionForm(request.POST, instance=section)
            else:
                about_form = AboutSectionForm(request.POST)

            if about_form.is_valid():
                about_form.save()
                messages.success(request, "About section saved.")
                about_form = AboutSectionForm()

        elif form_type == 'about_delete':
            about_pk = request.POST.get('about_pk')
            section = get_object_or_404(AboutSection, pk=about_pk)
            section.delete()
            messages.success(request, "About section deleted.")
            about_form = AboutSectionForm()

        elif request.POST.get('information') is not None:
            if category_form.is_valid():
                category_form.save()
                messages.success(request, "Category submitted!")
                category_form = CategoryForm()
        elif 'image' in request.FILES or request.POST.get('video') is not None:
            if media_form.is_valid():
                media_form.save()
                messages.success(request, "Media submitted!")
                media_form = MediaForm()
            else:
                print("media form is invalid:", media_form.errors)
        else:
            print("Unrecognized POST data")

    # include existing about sections so template can show edit/delete controls
    about_list = AboutSection.objects.all().order_by('-created_on')

    return render(
        request, 'gallery/admin_panel.html',
        {
            "category_form": category_form,
            "media_form": media_form,
            "about_form": about_form,
            "about_list": about_list
        }
    )

    # Handle category submission
def add_category(request):
    category_form = CategoryForm(data=request.POST)
    if category_form.is_valid():
        category = category_form.save(commit=False)
        category.save()
        messages.add_message(
            request, messages.SUCCESS, "Category submitted!"
        )

    # Handle Media Submission
def add_media(request):
    # pass request.FILES when constructing the form
    media_form = MediaForm(data=request.POST, files=request.FILES)
    if media_form.is_valid():
        media = media_form.save(commit=False)
        media.save()
        messages.add_message(
            request, messages.SUCCESS, "Media submitted!"
        )
    else:
        print("media form is invalid:", media_form.errors)
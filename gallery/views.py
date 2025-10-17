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

    # Prefill forms when GET includes edit params
    edit_pk = request.GET.get('edit')
    if edit_pk:
        section = get_object_or_404(AboutSection, pk=edit_pk)
        about_form = AboutSectionForm(instance=section)

    edit_cat = request.GET.get('edit_category')
    if edit_cat:
        category = get_object_or_404(Category, pk=edit_cat)
        category_form = CategoryForm(instance=category)

    edit_media = request.GET.get('edit_media')
    if edit_media:
        media_instance = get_object_or_404(Media, pk=edit_media)
        media_form = MediaForm(instance=media_instance)

    if request.method == "POST":
        form_type = request.POST.get('form_type')

        # category_form = CategoryForm(data=request.POST)
        # media_form = MediaForm(data=request.POST, files=request.FILES)
        # about_form = AboutSectionForm(data=request.POST)

        # Start (below): edit forms based only on which form was submitted
        if form_type == 'about':
            about_form = AboutSectionForm(data=request.POST)
            category_form = CategoryForm()
            media_form = MediaForm()
        elif form_type == 'category':
            category_form = CategoryForm(data=request.POST)
            about_form = AboutSectionForm()
            media_form = MediaForm()
        elif form_type == 'media':
            media_form = MediaForm(data=request.POST, files=request.FILES)
            about_form = AboutSectionForm()
            category_form = CategoryForm()
        else:
            # fallback: all unbound
            about_form = AboutSectionForm()
            category_form = CategoryForm()
            media_form = MediaForm()

        # End (above ^^ ): edit forms based only on which form was submitted

        # Below: process each form based on 'form_type'
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

        elif form_type == 'category':
            category_pk = request.POST.get('category_pk')
            if category_pk:
                category_inst = get_object_or_404(Category, pk=category_pk)
                category_form = CategoryForm(request.POST, instance=category_inst)
            else:
                category_form = CategoryForm(request.POST)

            if category_form.is_valid():
                category_form.save()
                messages.success(request, "Category saved.")
                category_form = CategoryForm()

        elif form_type == 'category_delete':
            category_pk = request.POST.get('category_pk')
            category = get_object_or_404(Category, pk=category_pk)
            category.delete()
            messages.success(request, "Category deleted.")
            category_form = CategoryForm()

        elif form_type == 'media':
            media_pk = request.POST.get('media_pk')
            if media_pk:
                media_inst = get_object_or_404(Media, pk=media_pk)
                media_form = MediaForm(request.POST, request.FILES, instance=media_inst)
            else:
                media_form = MediaForm(request.POST, request.FILES)

            if media_form.is_valid():
                media_form.save()
                messages.success(request, "Media saved.")
                media_form = MediaForm()

        elif form_type == 'media_delete':
            media_pk = request.POST.get('media_pk')
            media = get_object_or_404(Media, pk=media_pk)
            media.delete()
            messages.success(request, "Media deleted.")
            media_form = MediaForm()

        else:
            print("Unrecognized POST data")

    # include existing objects so template can show edit/delete controls
    about_list = AboutSection.objects.all().order_by('-created_on')
    category_list = Category.objects.all().order_by('list_position', 'pk')
    media_list = Media.objects.all().order_by('-created_on')

    return render(
        request, 'gallery/admin_panel.html',
        {
            "category_form": category_form,
            "media_form": media_form,
            "about_form": about_form,
            "about_list": about_list,
            "category_list": category_list,
            "media_list": media_list,
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
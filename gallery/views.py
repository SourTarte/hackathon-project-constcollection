from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Category, Media
from .forms import CategoryForm, MediaForm

# ------------------ Product Views ------------------ #


# class MediaList(generic.ListView):
#     """
#     Displays a list of all products.
#     """
#     queryset = Media.objects.all()
#     template_name = 'index.html'


# class ArtList(generic.ListView):
#     model = Media
#     template_name = "gallery/art_list.html"
#     context_object_name = "media_list"
#     paginate_by = 12

def welcome_view(request):
    return render(request, 'gallery/welcome.html')


# def art_view(request):
#     categories = Category.objects.all().order_by('list_position')
#     return render(request, 'gallery/art.html', {'categories': categories})

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
    # instantiate forms with POST/FILES when appropriate so errors remain visible
    if request.method == "POST":
        category_form = CategoryForm(data=request.POST)
        media_form = MediaForm(data=request.POST, files=request.FILES)

        # Decide which form was submitted by checking posted fields / files
        if request.POST.get('information') is not None:
            if category_form.is_valid():
                category = category_form.save()
                messages.success(request, "Category submitted!")
                category_form = CategoryForm()  # reset after success
            # else leave category_form with errors to render
        elif 'image' in request.FILES or request.POST.get('video') is not None:
            if media_form.is_valid():
                media = media_form.save()
                messages.success(request, "Media submitted!")
                media_form = MediaForm()  # reset after success
            else:
                # keep media_form with errors so template can show them
                print("media form is invalid:", media_form.errors)
        else:
            print("Unrecognized POST data")

    else:
        category_form = CategoryForm()
        media_form = MediaForm()

    return render(
        request, 'gallery/admin_panel.html',
        {"category_form": category_form, "media_form": media_form}
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
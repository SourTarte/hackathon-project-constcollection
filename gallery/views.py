from django.shortcuts import render
from django.contrib import messages
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


def admin_view(request):
    if request.method == "POST":
        category_form = CategoryForm(data=request.POST)
        media_form = MediaForm(data=request.POST)
        #Uses an if statement to determine which form was Submitted
        if request.POST.get('information') != None:
            print("This is a category")
            add_category(request)
        elif request.POST.get('image') != None:
            print("This is media")
            add_media(request)
        else: print("This is something else")
        
            
    # Always provide a fresh review form for GET or after POST
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
            request, messages.SUCCESS,
            'review submitted and awaiting approval'
        )

    # Handle Media Submission
def add_media(request):
    media_form = MediaForm(data=request.POST)
    if media_form.is_valid():
        media = media_form.save(commit=False)
        media.save()
        messages.add_message(
            request, messages.SUCCESS,
            'review submitted and awaiting approval'
        )
from django.shortcuts import render
from .models import Category, Media

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
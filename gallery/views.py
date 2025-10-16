from django.views import generic
from django.db.models import Prefetch
from .models import Media, Category

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


class ArtList(generic.TemplateView):
    queryset = Category.objects.all()
    template_name = "gallery/art_list.html"


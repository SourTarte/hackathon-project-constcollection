# from django.shortcuts import render, get_object_or_404, redirect
# from django.urls import reverse
from django.views import generic
from django.db.models import Prefetch
# from django.contrib import messages
# from django.http import HttpResponseRedirect
# from .forms import ReviewForm
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
    template_name = "gallery/art_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Prefetch media for each category, ordered by created_on
        media_qs = Media.objects.order_by('created_on').select_related('category')
        categories = Category.objects.prefetch_related(
            Prefetch('media', queryset=media_qs, to_attr='ordered_media')
        ).order_by('name')
        ctx['categories'] = categories
        return ctx


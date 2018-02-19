from django.shortcuts import render

# Create your views here.
from django.views import generic

from core.models import Organisation


class IndexView(generic.ListView):
    context_object_name = 'latest_organisation_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Organisation.objects.order_by('-date_created')[:5]


class DetailView(generic.DetailView):
    model = Organisation


class ResultsView(generic.DetailView):
    model = Organisation
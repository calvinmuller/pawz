from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Organisation

class IndexView(generic.ListView):
    context_object_name = 'latest_organisation_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Organisation.objects.all()[:5]


class DetailView(generic.DetailView):
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Organisation.objects.filter()


class ResultsView(generic.DetailView):
    model = Organisation

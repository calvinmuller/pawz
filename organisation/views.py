from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from core.models import Organisation
from pawz.mailer import Mailer


class IndexView(generic.ListView):
    context_object_name = 'latest_organisation_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Organisation.objects.order_by('-date_created')[:5]


class DetailView(generic.DetailView):
    model = Organisation


class PawView(generic.DetailView):
    model = Organisation
    template_name = 'paws/paw_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pawSlug = self.kwargs.get('paw')
        organisation = self.object
        # update_db.delay(organisation.id)
        context['paw'] = get_object_or_404(organisation.paw_set, slug=pawSlug)
        return context


class EmailView(generic.ListView):
    template_name = 'paws/paw_detail.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Organisation.objects.order_by('-date_created')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mail = Mailer()
        mail.send_messages(subject='My App account verification',
                           template='emails/customer_verification.html',
                           context={'customer': self},
                           to_emails=['calvin@istreet.co.za'])
        return context
# Django
from django.http import HttpResponseRedirect
from django.shortcuts import reverse


def home(request):
    return HttpResponseRedirect(reverse('latest_stories'))

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q, Sum, Count
from .models import *
from .forms import BejegyzesForm
# Create your views here.


def index(request):
    form = BejegyzesForm(request.POST or None)
    if(request.method == "POST"):
        if(form.is_valid()):
            form.save()
            form = BejegyzesForm()
    else:
        form = BejegyzesForm()


    osszpontszamok = Bejegyzes.objects.values('osztaly_id').annotate(osszpontszam = Sum('tevekenyseg_id_id__pontszam')).filter(Q(allapot__exact = 'Jóváhagyott')).order_by('-osszpontszam')
    bejegyzesek = Bejegyzes.objects.all()
    tevekenysegek = Tevekenyseg.objects.all()
    osztalyok = OSZTALY_CHOICES

    context = {
        'form' : form,
        'bejegyzesek' : bejegyzesek,
        'tevekenysegek' : tevekenysegek,
        'osztalyok' : osztalyok,
        'osszpontszamok' : osszpontszamok
    }


    return render(request, "index.html", context=context)


def bejegyzesek(request):
    bejegyzesek = Bejegyzes.objects.all()
    osztalyok = OSZTALY_CHOICES

    context = {
        'bejegyzesek' : bejegyzesek,
        'osztalyok' : osztalyok
    }

    return render(request, "bejegyzesek.html", context=context)

def bejegyzesekOsztalyId(request, osztaly_id):
    osztaly = None
    for key, value in OSZTALY_CHOICES:
        if(int(key) == osztaly_id - 1):
            osztaly = value

    bejegyzesek = Bejegyzes.objects.filter(Q(osztaly_id__exact = osztaly_id))
    context = {
        'osztaly' : osztaly,
        'bejegyzesek' : bejegyzesek
    }

    return render(request, "osztalyBejegyzesek.html", context=context)

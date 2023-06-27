from django.shortcuts import render
from Phonk.models import phonk_singer

def phonk_singers_page(request):
    context = {'phonkers' : phonk_singer.objects.all()}
    return render(request,
                  'phonk_singers.html',
                  context=context)


def phonk_singer_page(request, phonker_id):
    context = {'phonker': phonk_singer.objects.get(pk = phonker_id)}
    return render(request,
                  'phonker.html',
                  context=context)
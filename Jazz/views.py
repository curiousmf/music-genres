from django.shortcuts import render
from Jazz.models import jazz_singer

def jazz_singers_page(request):
    context = {'jazzers' : jazz_singer.objects.all()}
    return render(request,
                  'jazz_singers.html',
                  context=context)


def jazz_singer_page(request, jazzer_id):
    context = {'jazzer': jazz_singer.objects.get(pk = jazzer_id)}
    return render(request,
                  'jazzer.html',
                  context=context)
from django.shortcuts import render
from Rock.models import rock_singer

# Create your views here.
def rock_singers_page(request):
    context = {'rockers' : rock_singer.objects.all()}
    return render(request,
                  'rock_singers.html',
                  context=context)


def rock_singer_page(request, rocker_id):
    context = {'rocker': rock_singer.objects.get(pk = rocker_id)}
    return render(request,
                  'rocker.html',
                  context=context)
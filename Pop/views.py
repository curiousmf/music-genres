from django.shortcuts import render
from Pop.models import pop_singer

# Create your views here.
def pop_singers_page(request):
    context = {'poppers' : pop_singer.objects.all()}
    return render(request,
                  'pop_singers.html',
                  context=context)


def pop_singer_page(request, popper_id):
    context = {'popper': pop_singer.objects.get(pk = popper_id)}
    return render(request,
                  'popper.html',
                  context=context)
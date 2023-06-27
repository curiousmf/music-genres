from django.shortcuts import render
from Rap.models import rap_singer

# Create your views here.
def rap_singers_page(request):
    context = {'rappers' : rap_singer.objects.all()}
    return render(request,
                  'rap_singers.html',
                  context=context)


def rap_singer_page(request, rapper_id):
    context = {'rapper': rap_singer.objects.get(pk = rapper_id)}
    print(rapper_id)
    return render(request,
                  'rapper.html',
                  context=context)
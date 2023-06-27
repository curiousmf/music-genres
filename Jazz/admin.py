from django.contrib import admin
from Rap.models import rap_singer
from Phonk.models import phonk_singer
from Rock.models import rock_singer
from Pop.models import pop_singer
from Jazz.models import jazz_singer

# Register your models here.
admin.site.register(rap_singer)
admin.site.register(phonk_singer)
admin.site.register(rock_singer)
admin.site.register(pop_singer)
admin.site.register(jazz_singer)
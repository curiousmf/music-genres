from django.urls import path
from Phonk.views import phonk_singers_page, phonk_singer_page

urlpatterns = [
    path('', phonk_singers_page),
    path('<int:phonker_id>/', phonk_singer_page),
]

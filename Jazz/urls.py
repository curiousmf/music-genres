from django.urls import path
from Jazz.views import jazz_singers_page, jazz_singer_page

urlpatterns = [
    path('', jazz_singers_page),
    path('<int:jazzer_id>/', jazz_singer_page),
]

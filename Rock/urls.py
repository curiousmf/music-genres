from django.urls import path
from Rock.views import rock_singer_page, rock_singers_page
urlpatterns = [
    path('', rock_singers_page),
    path('<int:rocker_id>/', rock_singer_page),
]

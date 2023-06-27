from django.urls import path
from Rap.views import rap_singers_page, rap_singer_page

urlpatterns = [
    path('', rap_singers_page),
    path('<int:rapper_id>/', rap_singer_page),
]

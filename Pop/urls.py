from django.urls import path
from Pop.views import pop_singers_page, pop_singer_page

urlpatterns = [
    path('', pop_singers_page),
    path('<int:popper_id>/', pop_singer_page),
]

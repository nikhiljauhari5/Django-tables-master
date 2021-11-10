from django.urls import path
from . import views

urlpatterns = [
    # int = integers
    # str = strings
    # path = whole urls /
    # slug = hyphen-and_underscores_
    # UUID = universal unique identifier
    
    path('', views.home, name="home"),
    path('<int:year>/<str:month>', views.home, name="home"),
    path('events', views.all_events, name="list-events"),
]
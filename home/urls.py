from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="csdb-home"),
    path('about/', views.about, name='csdb-about'),
    path('show_submission/<submission_id>', views.show_submission , name="show-submission"),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="csdb-home"),
    path('learning', views.learning, name='csdb-learning'),
    path('news', views.news, name='csdb-news'),
    path('show_submission/<submission_id>', views.show_submission , name="show-submission"),
    path('networking',views.networking, name="learning-networking"),
    path('cstools',views.cstools, name="learning-cstools"),
    path('programming',views.programming, name="learning-programming"),
    path('csbasics',views.csbasics, name="learning-csbasics"),
    path('tutorial/<tutorial_id>', views.tutorial , name="show-tutorial"),
    path('forum', views.forum, name="csdb-forum"),


]

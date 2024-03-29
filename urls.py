from django.urls import path
from . import views
app_name = 'polls'

#un exemple est donné pour chaque url

urlpatterns = [
    # /polls/
    path('',views.index, name='index'),
    # /polls/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/1/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # /polls/1/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
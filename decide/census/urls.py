from django.urls import path, include
from .views import CensusView
from . import views


urlpatterns = [
    path('census', CensusView.as_view()),
    path('', views.CensusCreate.as_view(), name='census_create'),
    path('voters/', views.listVoters, name='census_voters'),
    path('voting/', views.selectVoting, name="select_voting"),
    path('<int:voting_id>/', views.CensusDetail.as_view(), name='census_detail'),
]

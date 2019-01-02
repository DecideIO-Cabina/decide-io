from django.urls import path, include
from .views import CensusView
from . import views


urlpatterns = [
    path('', views.CensusCreate.as_view(), name='census_create'),
    path('census/', views.selectVoting, name="select_voting"),
    path('reuse/', views.reuseCensus, name="reuse_census"),
    path('<int:voting_id>/', views.CensusDetail.as_view(), name='census_detail'),
]



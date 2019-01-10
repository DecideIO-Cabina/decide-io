from django.urls import path, include
from .views import CensusView
from .views import HomeView
from . import views


urlpatterns = [
    path('home', HomeView.as_view()),
    path('census', CensusView.as_view()),
    path('', views.CensusCreate.as_view(), name='census_create'),

    path('voters/', views.listVoters, name='census_voters'),
    path('voting/', views.selectVoting, name="select_voting"),

    path('census/', views.selectVotingReuse, name="select_voting_reuse"),
    path('reuse/', views.reuseCensus, name="reuse_census"),

    path('<int:voting_id>/', views.CensusDetail.as_view(), name='census_detail'),
    
    path('user/', views.filter, name='census_filter'),


    path('create', views.create, name='create'),
    path('create2', views.create2, name='create2'),

    path('exportcsv', views.ExportAsCSV, name='exportcsv'),
    path('exportjson', views.ExportAsJSON, name='exportjson'),
    path('exportexcel', views.ExportAsExcel, name='exportexcel'),
    
    path('import', views.ImportAs.as_view(), name = 'import'),
    path('importcsv', views.ImportAsCSV, name='importcsv'),
    path('importjson', views.ImportAsJSON, name='importjson'),

    
    
    

]



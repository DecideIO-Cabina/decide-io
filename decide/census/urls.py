from django.urls import path, include
from .views import CensusView
from . import views


urlpatterns = [
    path('census', CensusView.as_view()),
    path('', views.CensusCreate.as_view(), name='census_create'),
    path('<int:voting_id>/', views.CensusDetail.as_view(), name='census_detail'),
    path('exportcsv', views.ExportAsCSV, name='exportcsv'),
    path('exportjson', views.ExportAsJSON, name='exportjson'),
    path('exportexcel', views.ExportAsExcel, name='exportexcel'),
    
    path('import', views.ImportAs.as_view(), name = 'import'),
    path('importcsv', views.ImportAsCSV, name='importcsv'),
    path('importjson', views.ImportAsJSON, name='importjson'),
#     path('importexcel', views.ImportAsExcel, name='importexcel'),
    
    
    
]

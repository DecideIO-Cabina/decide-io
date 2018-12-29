from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from django.views.generic import TemplateView
from voting.models import Voting
from django.template import loader
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from .resources import CensusResource
from tablib import Dataset
from django.utils.datastructures import MultiValueDictKeyError
import json


from rest_framework.status import (
        HTTP_201_CREATED as ST_201,
        HTTP_204_NO_CONTENT as ST_204,
        HTTP_400_BAD_REQUEST as ST_400,
        HTTP_401_UNAUTHORIZED as ST_401,
        HTTP_409_CONFLICT as ST_409
)

from base.perms import UserIsStaff
from .models import Census

class CensusView(TemplateView):
    template_name = 'census/census.html'

def ExportAsCSV(request):
    
    template = loader.get_template('census/index.html')
    census_resource = CensusResource()
    dataset = census_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="census.csv"'
    return response

def ExportAsJSON(request):
    
    template = loader.get_template('census/index.html')
    census_resource = CensusResource()
    dataset = census_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="census.json"'
    return response

def ExportAsExcel(request):
    
    template = loader.get_template('census/index.html')
    census_resource = CensusResource()
    dataset = census_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="census.xls"'
    return response

class ImportAs(TemplateView):
    template_name = 'census/import.html'
    
def ImportAsCSV(request):
    if request.method == 'POST':
        census_resource = CensusResource()
        dataset = Dataset()
        
    try:
       new_censuss = request.FILES['myfile']
       imported_data = dataset.load(new_censuss.read().decode('utf-8'), format='csv')
       result = census_resource.import_data(dataset, dry_run=True)  # Test the data import
    
       if not result.has_errors():
           census_resource.import_data(dataset, dry_run=False)  # Actually import now
       return render(request, 'census/index.html')
    except:
       return render(request, 'census/import.html')

def ImportAsJSON(request):
    
    if request.method == 'POST':
        census_resource = CensusResource()
        dataset = Dataset()

    try:
       new_censuss = request.FILES['myfile']
       imported_data = dataset.load(new_censuss.read().decode('utf-8'), format='json')
       result = census_resource.import_data(dataset, dry_run=True)  # Test the data import
    
       if not result.has_errors():
           census_resource.import_data(dataset, dry_run=False)  # Actually import now
       return render(request, 'census/index.html')
    except:
       return render(request, 'census/import.html')

# def ImportAsExcel(request):
#     if request.method == 'POST':
#         census_resource = CensusResource()
#         dataset = Dataset()
#                 
#     try:
#        new_censuss = request.FILES['myfile']
#        for a in new_censuss.read().decode('Latin-1'):
#            print(a)
#            
#        imported_data = dataset.load(new_censuss.read().decode('ISO-8859-1'),  format='xlsx')
#        result = census_resource.import_data(dataset, dry_run=True)  # Test the data import 
#     
#        if not result.has_errors():
#            census_resource.import_data(dataset, dry_run=False)  # Actually import now
#        return render(request, 'census/index.html')
#     except MultiValueDictKeyError:
#        return render(request, 'census/import.html')
    
class CensusCreate(generics.ListCreateAPIView):
    permission_classes = (UserIsStaff,)

    def create(self, request, *args, **kwargs):
        voting_id = request.data.get('voting_id')
        voters = request.data.get('voters')
        try:
            for voter in voters:
                census = Census(voting_id=voting_id, voter_id=voter)
                census.save()
        except IntegrityError:
            return Response('Error try to create census', status=ST_409)
        return Response('Census created', status=ST_201)

    def list(self, request, *args, **kwargs):
        voting_id = request.GET.get('voting_id')
        voters = Census.objects.filter(voting_id=voting_id).values_list('voter_id', flat=True)
        return Response({'voters': voters})


class CensusDetail(generics.RetrieveDestroyAPIView):

    def destroy(self, request, voting_id, *args, **kwargs):
        voters = request.data.get('voters')
        census = Census.objects.filter(voting_id=voting_id, voter_id__in=voters)
        census.delete()
        return Response('Voters deleted from census', status=ST_204)

    def retrieve(self, request, voting_id, *args, **kwargs):
        voter = request.GET.get('voter_id')
        try:
            Census.objects.get(voting_id=voting_id, voter_id=voter)
        except ObjectDoesNotExist:
            return Response('Invalid voter', status=ST_401)
        return Response('Valid voter')

from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from voting.models import Voting
import simplejson
from rest_framework import generics
from django.shortcuts import render, get_object_or_404,HttpResponse,\
    _get_queryset
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
from voting.models import Voting

from django.contrib.auth.models import User

from django.db.models.base import Model
from django.shortcuts import render



class HomeView(TemplateView):
	template_name = 'census/index.html'
    

def selectVoting(request):
    votings= set()
    allVotings = Census.objects.all().values_list('voting_id', flat=True)
    for v in allVotings:
        voting = Voting.objects.filter(id=v)
        if voting:
            votings.add(voting[0])
    return render(request,'census/selectVoting.html', {'votings':votings})

def listVoters(request):
        voting_id = request.GET.get('voting_id')
        voters = set()
        voter_ids = Census.objects.filter(voting_id=voting_id).values_list('voter_id', flat=True)
        for v_id in voter_ids:
            voter = User.objects.filter(id=v_id)
            if voter:
                voters.add(voter[0])    
        return render(request, 'census/censusByVoting.html', {'voters': voters,'voting_id':voting_id})

def create(request):
   
    votings = Voting.objects.all()
    allUsers = User.objects.all()
    
    return render(request,'census/create.html', {'allUsers':allUsers, 'votings':votings})

def create2(request):
    voting_id = request.POST.get('voting')
    voters = request.POST.getlist('voters')

    for voter in voters:
        census = Census(voting_id=voting_id, voter_id=voter)
        census.save()
    
    template = loader.get_template('census/index.html')
    context = {
        
        }
    
    return HttpResponse(template.render(context, request))


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
       return render(request, 'census/index.html')

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
       return render(request, 'census/index.html')


def selectVotingReuse(request):
    votings = set()
    votingsList = list()
    allVotingsWithCensus = Census.objects.all().values_list('voting_id', flat=True)
    
    for v in allVotingsWithCensus:
        votings.add(v)
    
    for v in Voting.objects.all().values_list('id', flat=True):
        votingsList.append(v)
    
    for v in votings:
        if v in votingsList:
            votingsList.remove(v)
    
    return render(request,'census/census.html', {'votings':votings, 'votingsW':votingsList})


def reuseCensus(request):
        voting_id_antiguo= request.GET.get('voting_id_antiguo')
        voting_id_nuevo = request.GET.get('voting_id_nuevo')
        
        voters = Census.objects.filter(voting_id=voting_id_antiguo).values_list('voter_id', flat=True)
        
        for voter in voters:
            census = Census(voting_id=voting_id_nuevo, voter_id=voter)
            census.save()
        return render(request, 'census/censoNuevo.html', {'voters': voters , 'voting_id':voting_id_nuevo})

    
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
    

def filter(request):
    voter_id = request.GET.get('user_id')
    votings = []
    voting_id = Census.objects.filter(voter_id=voter_id).values_list('voting_id', flat=True)
    for v in voting_id:
        votings.append(v)           
    json_stuff = simplejson.dumps({"list_of_votings_id" : votings})  
    return HttpResponse(json_stuff, content_type ="application/json")

  
        

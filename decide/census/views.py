from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from django.views.generic import TemplateView
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
from django.db.models.base import Model
from django.shortcuts import render

class CensusView(TemplateView):
    template_name = 'census/census.html'

def selectVoting(request):
    votings = set()
    votingsList = list()
    allVotingsWithCensus = Census.objects.all().values_list('voting_id', flat=True)
    
    for v in allVotingsWithCensus:
        votings.add(v)
    
    for v in Voting.objects.all().values_list('id', flat=True):
        votingsList.append(v)
    
    for v in votings:
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

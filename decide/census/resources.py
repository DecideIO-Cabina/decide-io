'''
Created on 9 dic. 2018

@author: migue
'''
from import_export import resources
from .models import Census

class CensusResource(resources.ModelResource):

    class Meta:
        model = Census
        fields = ('id','voting_id', 'voter_id')
        export_order = ('id','voting_id', 'voter_id')
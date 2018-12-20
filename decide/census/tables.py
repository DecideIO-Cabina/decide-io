'''
Created on 9 dic. 2018

@author: migue
'''
import django_tables2 as tables
from .models import Census


class CensoTable(tables.Table):
    class Meta:
        model = Census
        template_name = 'django_tables2/bootstrap.html'
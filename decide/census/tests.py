import random
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Census
from base import mods
from base.tests import BaseTestCase
from django.core.files import File
import re
import os
import sys

class CensusTestCase(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.census = Census(voting_id=1, voter_id=1)
        self.census.save()

    def tearDown(self):
        super().tearDown()
        self.census = None

    def test_check_vote_permissions(self):
        response = self.client.get('/census/{}/?voter_id={}'.format(1, 2), format='json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), 'Invalid voter')

        response = self.client.get('/census/{}/?voter_id={}'.format(1, 1), format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Valid voter')

    def test_list_voting(self):
        response = self.client.get('/census/?voting_id={}'.format(1), format='json')
        self.assertEqual(response.status_code, 401)

        self.login(user='noadmin')
        response = self.client.get('/census/?voting_id={}'.format(1), format='json')
        self.assertEqual(response.status_code, 403)

        self.login()
        response = self.client.get('/census/?voting_id={}'.format(1), format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'voters': [1]})

    def test_add_new_voters_conflict(self):
        data = {'voting_id': 1, 'voters': [1]}
        response = self.client.post('/census/', data, format='json')
        self.assertEqual(response.status_code, 401)

        self.login(user='noadmin')
        response = self.client.post('/census/', data, format='json')
        self.assertEqual(response.status_code, 403)

        self.login()
        response = self.client.post('/census/', data, format='json')
        self.assertEqual(response.status_code, 409)

    def test_add_new_voters(self):
        data = {'voting_id': 2, 'voters': [1,2,3,4]}
        response = self.client.post('/census/', data, format='json')
        self.assertEqual(response.status_code, 401)

        self.login(user='noadmin')
        response = self.client.post('/census/', data, format='json')
        self.assertEqual(response.status_code, 403)

        self.login()
        response = self.client.post('/census/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(data.get('voters')), Census.objects.count() - 1)
        
    def test_reuse_census(self):
        response = self.client.get('/census/reuse/?voting_id_antiguo={}&voting_id_nuevo={}'.format(1, 2),format='json')
        nVoters= Census.objects.filter(voting_id=1).count()
        self.assertEquals(nVoters,Census.objects.filter(voting_id=2).count())
        
    def test_destroy_voter(self):
        data = {'voters': [1]}
        response = self.client.delete('/census/{}/'.format(1), data, format='json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(0, Census.objects.count())
        
        
    def test_list_voters_view(self):
        response = self.client.get('/census/voters/?voting_id={}'.format(1))
        self.assertEqual(response.status_code, 200)
        
    def test_select_voting_view(self):
        response = self.client.get('/census/voting/')
        self.assertEqual(response.status_code, 200)
        
    def test_export_csv(self):
        prueba = Census(voting_id=200,voter_id=201)
        prueba.save()
        
        response = self.client.get('/census/exportcsv') #Si no va, probar anadir format='json' en los param
        pattern = re.compile("^.*\d+,200,201.*$")
        self.assertTrue(pattern.match(str(response.content)))
       
    def test_export_json(self):
        prueba = Census(voting_id=200,voter_id=201)
        prueba.save()
        
        response = self.client.get('/census/exportjson') #Si no va, probar anadir format='json' en los param
        pattern = re.compile('^.*{"id": \d+, "voting_id": 200, "voter_id": 201}.*$')
        self.assertTrue(pattern.match(str(response.content)))
        
    def test_export_excel(self):
        prueba = Census(voting_id=200,voter_id=201)
        prueba.save()
        
        response = self.client.get('/census/exportexcel') #Si no va, probar anadir format='json' en los param
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.has_header("Content-Disposition"))
        self.assertEqual(response['Content-Type'], 'application/vnd.ms-excel')
        
    def test_import_csv(self):
        files = {'upload_file': open(os.path.join(sys.path[0], "census\\testFiles\\census.csv"),'rb')}
        response = self.client.post('/census/importcsv', files = files)
        self.assertIsNotNone(Census.objects.filter(voting_id=200, voter_id=201))
        
    def test_import_json(self):
        files = {'upload_file': open(os.path.join(sys.path[0], "census\\testFiles\\census.json"),'rb')}
        response = self.client.post('/census/importjson', files = files)
        self.assertIsNotNone(Census.objects.filter(voting_id=200, voter_id=201))
        

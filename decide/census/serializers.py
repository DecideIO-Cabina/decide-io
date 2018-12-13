from rest_framework import serializers

class CensusSerializer(serializers.Serializer):
    voting_id = serializers.IntegerField()
    voter_id = serializers.IntegerField()
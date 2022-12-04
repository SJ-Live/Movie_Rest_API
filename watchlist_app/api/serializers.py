from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, vaidated_data):
        return Movie.objects.create(**vaidated_data)

    def update(self, instance, vaidated_data):
        instance.name = vaidated_data.get('name', instance.name)
        instance.description = vaidated_data.get('description', instance.description)
        instance.active = vaidated_data.get('active', instance.active)
        instance.save()
        return instance
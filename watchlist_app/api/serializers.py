from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatform




class WatchListSerializer(serializers.ModelSerializer):
    
     class Meta:
        model = Watchlist
        fields = "__all__"
        #fields = ['id', 'name', 'description']
        #exclude = ['name']

# HyperlinkedModelSerializer is use the link of the model instead of pk

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer): 
    """This is an example of nester serializer. Here watchlist is the related name we defined in models.py
    Now StreamPlatformSerializer can have all the shows in the WatchListSerializer"""
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"

#     def get_len_name(self, obj):
#         return len(obj.name)

#     #Object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Movie name cannot be the same as description')
#         else:
#             return data    

#    # Field level validation
#     def validate_name(self, value):
#         if len(value) < 2 :
#             raise serializers.ValidationError('Name is too short')
#         else:
#             return value

#def name_length(value):
#     if len(value) < 2 :
#         raise serializers.ValidationError('Name is too short')


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, vaidated_data):
#         return Movie.objects.create(**vaidated_data)

#     def update(self, instance, vaidated_data):
#         instance.name = vaidated_data.get('name', instance.name)
#         instance.description = vaidated_data.get('description', instance.description)
#         instance.active = vaidated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     #Object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Movie name cannot be the same as description')
#         else:
#             return data    

    # Field level validation
    # def validate_name(self, value):
    #     if len(value) < 2 :
    #         raise serializers.ValidationError('Name is too short')
    #     else:
    #         return value

    

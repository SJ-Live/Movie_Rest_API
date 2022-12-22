from watchlist_app.models  import Watchlist, StreamPlatform
from watchlist_app.api.serializers import StreamPlatformSerializer, WatchListSerializer
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


class StreamPlatformAV(APIView):

  def get(self, request):
    platform = StreamPlatform.objects.all()
    serializer = StreamPlatformSerializer(platform, many=True, context= {'request': request}) # context is used for hyper linked model serialization
    return Response(serializer.data)

  def post(self, request):
      serializer = StreamPlatformSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      else:
          return Response(serializer.errors)

class StreamDetailAV(APIView):
    def get(self, request, pk):
      try:
          platform = StreamPlatform.objects.get(pk=pk)
      except StreamPlatform.DoesNotExist:
          return Response({'Error': 'Not found'}, status=status.HTTP_404_NOT_FOUND) 
      serializer = StreamPlatformSerializer(platform, context= {'request': request}) # context is used for hyper linked model serialization
      return Response(serializer.data)

    def put(self, request, pk):
      platform = StreamPlatform.objects.get(pk=pk)
      serializer = StreamPlatformSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      else:
          return Response(serializer.errors)

    def delete(self, request, pk):
      movie = StreamPlatform.objects.get(pk=pk)
      movie.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)


class WatchlistAV(APIView):
  def get(self, request):
    movies = Watchlist.objects.all()
    serializer = WatchListSerializer(movies, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = WatchListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors) 

class WatchDetailAV(APIView):

  def get(self, request, pk):
    try:
      movie = Watchlist.objects.get(pk=pk)
    except Watchlist.DoesNotExist:
      return Response({'Error': 'Not found'}, status=status.HTTP_404_NOT_FOUND) 
    serializer = WatchListSerializer(movie)
    return Response(serializer.data)
  
  def put(self, request, pk):
    movie = Watchlist.objects.get(pk=pk)
    serializer = WatchListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

  def delete(self, request, pk):
    movie = Watchlist.objects.get(pk=pk)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def movie_list(request):
#   if request.method == 'GET':
#     movies = Movie.objects.all()
#     serializer = WatchListSerializer(movies, many=True)
#     return Response(serializer.data)
  
#   if request.method == 'POST':
#     serializer = WatchListSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)    


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def movie_details(request,pk):
#   if request.method == 'GET':
#     try:
#       movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#       return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND) 
#     serializer = WatchListSerializer(movie)
#     return Response(serializer.data)
  
  
#   if request.method == 'PUT':
#       movie = Movie.objects.get(pk=pk)
#       serializer = WatchListSerializer(movie, data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)
#       else:
#           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
#   if request.method == 'DELETE':
#       movie = Movie.objects.get(pk=pk)
#       movie.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)  
from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchlistAV, WatchDetailAV, StreamPlatformAV,StreamDetailAV


urlpatterns = [
    path('list/', WatchlistAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name='streamplatform-detail'),
]
from django.urls import path, include
# from watchlist_app.api.views import movie_list , movie_details
from watchlist_app.api.views import  WatchListAV, WatchDetailAV, StreamPlatformAV ,StreamPlatformDetailAV, ReviewList, ReviewDetail
urlpatterns = [
    # function based views
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie-details')
    
    #class based views
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    path('review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')

]

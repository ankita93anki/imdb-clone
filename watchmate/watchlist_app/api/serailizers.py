from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchList = serializers.HyperlinkedRelatedField(source="watchlist",many=True, read_only=True, view_name='movie-details')
    class Meta:
        model = StreamPlatform
        fields = "__all__"
  

from rest_framework import serializers

from todo.models import *

class FinishTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinishTimeClass
        fields='__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoClass
        fields='__all__'


class PlaylistSerializer(serializers.ModelSerializer):
    playlist = TodoSerializer(required=False,allow_null=True)
    finished = FinishTimeSerializer(required=False,allow_null=True)

    class Meta:
        model = PlayListClass
        fields='__all__'
    
    def update(self, instance, validated_data):
        print(validated_data)
        title=validated_data.get('title')
        temp=instance[0]

        temp.title=validated_data.get('title')
        print(temp.title)
        temp.save()

        playlist_data = validated_data.get('playlist', None)
        if playlist_data:
            playlist = instance[0].playlist
            playlist.title=playlist_data.get('title')
            playlist.description=playlist_data.get('description')
            playlist.create_time=playlist_data.get('create_time')
            playlist.star=playlist_data.get('star')
            playlist.finished=playlist_data.get('finished')
            playlist.save()

        finish_time_data=validated_data.get('finished')
        if finish_time_data:
            finished=instance[0].finished
            finished.finish_time=finish_time_data.get('finish_time')
            finished.save()

        return instance[0]

class MyDaySerializer(serializers.ModelSerializer):
    playlist = TodoSerializer()

    class Meta:
        model = MyDayClass
        fields='__all__'

    def update(self, instance, validated_data):
        playlist_data = validated_data.get('playlist', None)
        playlist = instance[0].playlist
        playlist.title=playlist_data.get('title')
        playlist.description=playlist_data.get('description')
        playlist.create_time=playlist_data.get('create_time')
        playlist.star=playlist_data.get('star')
        playlist.finished=playlist_data.get('finished')
        playlist.save()
        
        return instance[0]


class ImportantSerializer(serializers.ModelSerializer):
    playlist = TodoSerializer()
    # finished = FinishTimeSerializer()

    class Meta:
        model = ImportantClass
        fields='__all__'

    def update(self, instance, validated_data):
        playlist_data = validated_data.get('playlist', None)
        playlist = instance[0].playlist
        playlist.title=playlist_data.get('title')
        playlist.description=playlist_data.get('description')
        playlist.create_time=playlist_data.get('create_time')
        playlist.star=playlist_data.get('star')
        playlist.finished=playlist_data.get('finished')
        playlist.save()
        
        return instance[0]
        


class PlanSerializer(serializers.ModelSerializer):
    playlist = TodoSerializer()
    finished = FinishTimeSerializer()

    class Meta:
        model = PlanClass
        fields='__all__'

    def update(self, instance, validated_data):
        playlist_data = validated_data.get('playlist', None)
        playlist = instance[0].playlist
        playlist.title=playlist_data.get('title')
        playlist.description=playlist_data.get('description')
        playlist.create_time=playlist_data.get('create_time')
        playlist.star=playlist_data.get('star')
        playlist.finished=playlist_data.get('finished')
        playlist.save()

        finish_time_data=validated_data.get('finished')
        finished=instance[0].finished
        finished.finish_time=finish_time_data.get('finish_time')
        finished.save()

        return instance[0]
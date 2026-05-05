from rest_framework import serializers
from .models import Confession, Reaction,Comment

class ConfessionSerializer(serializers.ModelSerializer):
    reaction_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Confession
        fields = ['id', 'content', 'created_at', 'reaction_count', 'comment_count']

    def get_reaction_count(self, obj):
        return obj.reaction_set.count()

    def get_comment_count(self, obj):
        return obj.comment_set.count()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = '__all__' all deoya mane shob gula required field
        fields = ['id', 'content', 'created_at']
        read_only_fields = ['ip_hash', 'created_at']
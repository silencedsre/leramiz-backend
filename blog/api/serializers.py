from rest_framework import serializers
from blog.models import CommentModel
class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('author', 'comment')
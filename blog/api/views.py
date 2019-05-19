from rest_framework import generics
from blog.models import CommentModel
from .serializers import CommentModelSerializer
class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentModelSerializer
    def get_queryset(self):
        return CommentModel.objects.all()

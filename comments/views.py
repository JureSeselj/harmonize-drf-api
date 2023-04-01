from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from harmonize_drf_api.permissions import IsOwnerOrReadOnly


class CommentList(generics.ListCreateAPIView):
    """
    A class for ClassList to view all the comments
    """
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class for CommentDetail
    User to be able to retrieve, edit and delete their comment
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [
        IsOwnerOrReadOnly
        ]
    queryset = Comment.objects.all()

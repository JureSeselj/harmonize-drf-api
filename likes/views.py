from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer
from harmonize_drf_api.permissions import IsOwnerOrReadOnly


class LikeList(generics.ListCreateAPIView):
    """
    A class for LikeList
    """
    serializer_class = LikeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        # owner is the user making the request
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    A class for LikeDetail
    User to be able to retrieve and delete their like
    """
    serializer_class = LikeSerializer
    permission_classes = [
        IsOwnerOrReadOnly
        ]
    queryset = Like.objects.all()

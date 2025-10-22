from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly

# from drf_spectacular.utils import extend_schema

# @extend_schema(
#     summary="List, create, and manage blog posts",
#     tags=["Posts"]
# )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete user's token to log them out
        request.user.auth_token.delete()
        return Response({"detail": "Successfully logged out and token deleted."})
    
class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset =  Post.objects.select_related("author").all().order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    search_fields = ['post_title', 'post_body', 'author__email']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

from  django.views.decorators.csrf import csrf_exempt

class PostListCreate(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('-id')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from restapp.models import Post
from . serializers import PostSerializer


class PostList(APIView):

    def get(self, request):
        allpost = Post.objects.all()
        serializer = PostSerializer(allpost, many=True)
        return Response(serializer.data)

    def post(self):
        pass

from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models import Post, Group, Comment

from .serializers import PostSerializer, GroupSerializer, CommentSerializer


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif (self.action == 'update'
              or self.action == 'partial_update'
              or self.action == 'destroy'):
            return [permissions.IsAuthenticated(), IsOwner()]
        elif self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET', 'POST'])
def api_comment(request, post_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_403_FORBIDDEN)
        post = get_object_or_404(Post, id=post_id)
        data = request.data
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    comments = Comment.objects.filter(post__pk=post_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_comment_detail(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'GET':
        if not permissions.IsAuthenticated():
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    if request.method == 'PUT' or request.method == 'PATCH':
        user = request.user
        if user != comment.author:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment,
                                       data=request.data,
                                       partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user = request.user
        if user != comment.author:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return comment.delete()

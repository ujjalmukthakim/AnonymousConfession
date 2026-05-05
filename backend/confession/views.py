
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Reaction, Confession,Comment
from .serializers import ConfessionSerializer,CommentSerializer
import hashlib
from django.utils import timezone
from datetime import timedelta


def get_ip_hash(request):
    ip = request.META.get('REMOTE_ADDR')
    return hashlib.sha256(ip.encode()).hexdigest()


@api_view(['GET', 'POST'])
def confessions(request):
    if request.method == 'POST':
        serializer = ConfessionSerializer(data=request.data)

        if serializer.is_valid():
            ip_hash = get_ip_hash(request)

            one_hour_ago = timezone.now() - timedelta(hours=1)

            count = Confession.objects.filter(
             ip_hash=ip_hash,
              created_at__gte=one_hour_ago
              ).count()

            if count >= 3:
                 return Response(
                     {"error": "Rate limit exceeded. Try again later."},
                     status=429
                 )
            serializer.save(ip_hash=get_ip_hash(request))
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    elif request.method == 'GET':
        confs = Confession.objects.all()
        serializer = ConfessionSerializer(confs, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
def react_confession(request, confession_id):
    try:
        confession = Confession.objects.get(id=confession_id)
    except Confession.DoesNotExist:
        return Response({"error": "Confession not found"}, status=404)

    ip_hash = get_ip_hash(request)

    # Check if already reacted
    if Reaction.objects.filter(confession=confession, ip_hash=ip_hash).exists():
        return Response({"error": "You already reacted"}, status=400)

    # Create reaction
    Reaction.objects.create(confession=confession, ip_hash=ip_hash)

    return Response({"message": "Reaction added"})



@api_view(['POST'])
def add_comment(request, confession_id):
    try:
        confession = Confession.objects.get(id=confession_id)
    except Confession.DoesNotExist:
        return Response({"error": "Confession not found"}, status=404)

    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(
            confession=confession,
            ip_hash=get_ip_hash(request)
        )
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_comments(request, confession_id):
    try:
        confession = Confession.objects.get(id=confession_id)
    except Confession.DoesNotExist:
        return Response({"error": "Confession not found"}, status=404)

    comments = Comment.objects.filter(confession=confession).order_by('-created_at')
    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data)


@api_view(['DELETE'])
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return Response({"error": "Comment not found"}, status=404)

    user_ip_hash = get_ip_hash(request)

    # Ownership check
    if comment.ip_hash != user_ip_hash:
        return Response({"error": "Not allowed"}, status=403)

    comment.delete()
    return Response({"message": "Comment deleted"})
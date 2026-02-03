from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Goal
from rest_framework import status

@api_view(['POST'])
def register_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "username and password required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "user already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    return Response({"message": "user created", "username": user.username}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_goal(request):
    title = request.data.get("title")
    if not title:
        return Response({"error": "title required"}, status=status.HTTP_400_BAD_REQUEST)

    goal, _ = Goal.object.update_or_create(user=request.user, title=title)
    return Response({"message": "goal created", "title": goal.title}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_goals(request):
    goals = Goal.objects.filter(user=request.user).order_by("-created_at")
    data = [{"id": g.id, "title": g.title, "created_at": g.created_at} for g in goals]
    return Response({"goals": data})
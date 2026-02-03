from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Quest, DailyProgress
from rest_framework import serializers

class QuestStatusSerializer(serializers.ModelSerializer):
    is_completed = serializers.SerializerMethodField()

    class Meta:
        model = Quest
        fields = ['id', 'title', 'category', 'is_completed']

    def get_is_completed(self, obj):
        user = self.context['request'].user
        if user.is_anonymous:
            return False
        return DailyProgress.objects.filter(
            user=user, 
            quest=obj, 
            date=timezone.now().date(), 
            is_completed=True
        ).exists()
class TodayStatusView(APIView):
    def get(self, request):
        quests = Quest.objects.all().order_by('order')
        serializer = QuestStatusSerializer(quests, context={'request': request})
        
        total_count = quests.count()
        completed_count = sum(1 for q in serializer.data if q['is_completed'])

        return Response({
            'total_quests': total_count,
            'completed_count': completed_count,
            'quests': serializer.data
        })
class ReportProgressView(APIView):
    def post(self, request):
        quest_id = request.data.get('quest_id')
        is_completed = request.data.get('is_completed')
        reason = request.data.get('failure_reason', "")

        progress, created = DailyProgress.objects.update_or_create(
            user=request.user,
            quest_id=quest_id,
            date=timezone.now().date(),
            defaults={
                'is_completed': is_completed,
                'failure_reason': reason
            }
        )
        return Response({"status": "success"})

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User 

class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.create_user(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "認証に失敗しました"}, status=status.HTTP_401_UNAUTHORIZED)
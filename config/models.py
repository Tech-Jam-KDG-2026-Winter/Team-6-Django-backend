from django.db import models
from django.conf import settings

class Quest(models.Model):
    """
    ユーザーに課される個別のタスク
    """
    CATEGORY_CHOICES = [('exercise', '運動'), ('care', 'お世話')]
    
    title = models.CharField("タイトル", max_length=100)
    category = models.CharField("カテゴリ", max_length=20, choices=CATEGORY_CHOICES)
    order = models.IntegerField("表示順", default=0)

    def __str__(self):
        return self.title

class DailyProgress(models.Model):
    """
    「誰が」「いつ」「どのクエストを」達成したか、あるいはサボったか
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    date = models.DateField("実施日", auto_now_add=True)
    is_completed = models.BooleanField("達成フラグ", default=False)
    failure_reason = models.CharField("サボり理由", max_length=255, blank=True, null=True)


    class Meta:
        unique_together = ('user', 'quest', 'date','is_completed','failure_reason')
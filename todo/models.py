from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User

# Create your models here.


class TodoClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    title=models.CharField(max_length=100,verbose_name='title',name='title')
    description=models.TextField(verbose_name='description',blank=True)
    create_time=models.DateTimeField(default=timezone.now)
    star=models.BooleanField(default=False,verbose_name='Star')
    finished=models.BooleanField(default=False,verbose_name='Finished')

    def __str__(self):
        return self.title
    
class FinishTimeClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    finish_time=models.DateTimeField(auto_now=False, auto_now_add=False,blank=True)

    def __str__(self):
        return self.finish_time.strftime("%Y-%m-%d %H:%M:%S")


class MyDayClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    user=models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE,null=True)
    playlist=models.ForeignKey(TodoClass, verbose_name="myday", on_delete=models.CASCADE)
    finished=None

    class Meta:
        verbose_name='myday'
        verbose_name_plural='myday'

    def __str__(self):
        return self.playlist.title


class ImportantClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    user=models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE,null=True)
    playlist=models.ForeignKey(TodoClass, verbose_name="important", on_delete=models.CASCADE)
    finished=None

    class Meta:
        verbose_name='important'
        verbose_name_plural='important'

    def __str__(self):
        return self.playlist.title


class PlanClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    user=models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    playlist=models.ForeignKey(TodoClass, verbose_name="plan", on_delete=models.CASCADE)
    finished=models.ForeignKey(FinishTimeClass, verbose_name="plan_finish", on_delete=models.CASCADE)

    def save(self,*args, **kwargs):
        finish_time=self.finished.finish_time
        created_time=self.playlist.create_time
        if created_time > finish_time:
            raise ValueError("finished time should be in future")
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name='plan'
        verbose_name_plural='plan'

    def __str__(self):
        return self.playlist.title


class PlayListClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    user=models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=50)
    playlist=models.ForeignKey(TodoClass, verbose_name="plan", on_delete=models.CASCADE,blank=True,null=True)
    finished=models.ForeignKey(FinishTimeClass, verbose_name="playlist_finished", on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        verbose_name='playlist'
        verbose_name_plural='playlists'

    def __str__(self):
        return self.title


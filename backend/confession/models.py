from django.db import models
import uuid

# Create your models here.

class Confession(models.Model):

    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ip_hash = models.CharField(max_length=255)

    class Meta:
        ordering=['-created_at']
        
    def __str__(self):
        return self.content[:30]
    
class Reaction(models.Model):
    confession = models.ForeignKey(Confession, on_delete=models.CASCADE)
    ip_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta :
     unique_together = ('confession', 'ip_hash')


class Comment(models.Model):
    confession = models.ForeignKey(Confession, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    ip_hash = models.CharField(max_length=255)
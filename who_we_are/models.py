from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.CharField(verbose_name="Question", max_length=250)
    answer = RichTextField()
    created_at = models.DateField(default=timezone.now)

    class Meta:
        verbose_name_plural = "FAQs"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.question

class TeamMember(models.Model):
    name = models.CharField(verbose_name="Full Name", max_length=250)
    position = models.CharField(verbose_name="Position", max_length=250)
    image = models.ImageField(verbose_name="Image", upload_to="team/")
    rank = models.IntegerField(verbose_name="Rank", default=0)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
from django.db import models
from django.utils import timezone


class EconomicsAdvocacy(models.Model):
    overview = models.TextField(verbose_name="Overview")
    importance = models.TextField(verbose_name="Importance", null=True, blank=True)
    conclusion = models.TextField(verbose_name="Conclusion", null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Economics Advocacy"
    
    def __str__(self):
        return self.overview

class Governance(models.Model):
    overview = models.TextField(verbose_name="Overview")
    importance = models.TextField(verbose_name="Importance", null=True, blank=True)
    conclusion = models.TextField(verbose_name="Conclusion", null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Governance"
    
    def __str__(self):
        return self.overview
    
class SocialAccountability(models.Model):
    overview = models.TextField(verbose_name="Overview")
    importance = models.TextField(verbose_name="Importance", null=True, blank=True)
    conclusion = models.TextField(verbose_name="Conclusion", null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Social Development"
    
    def __str__(self):
        return self.overview
        
class ParliamentaryMonitoring(models.Model):
    overview = models.TextField(verbose_name="Overview")
    importance = models.TextField(verbose_name="Importance", null=True, blank=True)
    conclusion = models.TextField(verbose_name="Conclusion", null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Parliamentary Monitoring"
    
    def __str__(self):
        return self.overview
    
class HealthAdvocacy(models.Model):
    overview = models.TextField(verbose_name="Overview")
    importance = models.TextField(verbose_name="Importance", null=True, blank=True)
    conclusion = models.TextField(verbose_name="Conclusion", null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Health Advocacy"
    
    def __str__(self):
        return self.overview


from django.shortcuts import render, get_object_or_404
from .models import EconomicsAdvocacy, Governance, SocialAccountability, ParliamentaryMonitoring, HealthAdvocacy
from news_and_media.models import Release

def focus_areas(request):
    economics = EconomicsAdvocacy.objects.all()
    governance = Governance.objects.all()
    social = SocialAccountability.objects.all()
    parliamentary = ParliamentaryMonitoring.objects.all()
    health = HealthAdvocacy.objects.all()
    
    #press_releases = Release.objects.filter(tag='Press Release')[:10]
    
    return render(request, 'focus.html')
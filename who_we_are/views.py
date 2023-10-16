from django.shortcuts import render
from .models import FAQ, TeamMember

def who_we_are(request):
    faqs = FAQ.objects.all()
    members = TeamMember.objects.all()
    return render(request, 'who_we_are.html', {'faqs': faqs, 'members': members})


def about(request):
    members = TeamMember.objects.all().order_by('rank')
    
    return render(request, 'about.html', {'members': members})




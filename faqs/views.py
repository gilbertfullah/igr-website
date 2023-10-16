from django.shortcuts import render
from who_we_are.models import FAQ

def faq(request):
    faqs = FAQ.objects.all()
    
    context = {
        'faqs': faqs
        }
    
    return render(request, 'faqs.html', context)

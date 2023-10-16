from django.contrib import admin
from .models import FAQ, TeamMember

class FAQsAdmin(admin.ModelAdmin):
    list_display = ['question']
    list_per_page = 10
    
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10

admin.site.register(FAQ, FAQsAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
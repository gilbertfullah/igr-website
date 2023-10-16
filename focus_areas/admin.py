from django.contrib import admin
from .models import EconomicsAdvocacy, Governance, SocialAccountability, ParliamentaryMonitoring, HealthAdvocacy

class EconomicsAdvocacyAdmin(admin.ModelAdmin):
    list_display = ['overview']
    
class GovernanceAdmin(admin.ModelAdmin):
    list_display = ['overview']

class SocialAccountabilityAdmin(admin.ModelAdmin):
    list_display = ['overview']
    
class ParliamentaryMonitoringAdmin(admin.ModelAdmin):
    list_display = ['overview']

class HealthAdvocacyAdmin(admin.ModelAdmin):
    list_display = ['overview']

admin.site.register(EconomicsAdvocacy, EconomicsAdvocacyAdmin)
admin.site.register(Governance, GovernanceAdmin)
admin.site.register(SocialAccountability, SocialAccountabilityAdmin)
admin.site.register(ParliamentaryMonitoring, ParliamentaryMonitoringAdmin)
admin.site.register(HealthAdvocacy, HealthAdvocacyAdmin)

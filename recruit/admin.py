from django.contrib import admin
from .models import Company, Member, Recruit, AppliedHistory
# Register your models here.

admin.site.register(Company)
admin.site.register(Member)
admin.site.register(Recruit)
admin.site.register(AppliedHistory)
from django.contrib import admin
from .models import Certificate,CertificateTemplates
# Register your models here.
class CertificateAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(Certificate,CertificateAdmin)
admin.site.register(CertificateTemplates)

from django.db import models
from django.utils.timezone import now
import uuid
# Create your models here.
from datetime import timedelta 
from django.utils import timezone
from django.core.validators import FileExtensionValidator
def return_date_time():
    now = timezone.now()
    return now + timedelta(days=365)
class CertificateTemplates(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='certificates/',validators=[FileExtensionValidator(allowed_extensions=['html'])])
    description = models.TextField(max_length=500)
    def __str__(self):
        return self.name
        
class Certificate(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(default=now)
    expiry = models.DateTimeField(default=return_date_time)
    certificate_template = models.ForeignKey(CertificateTemplates, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


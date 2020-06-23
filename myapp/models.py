from django.db import models
from django.utils import timezone
# Create your models here.

class ExcelData(models.Model):
    all_record  =   models.CharField(max_length=255, null=True, blank=True)
    file_name   =   models.CharField(max_length=255, null=True, blank=True)
    created_at  =   models.DateTimeField(default=timezone.now)
    updated_at  =   models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = "excel_data"
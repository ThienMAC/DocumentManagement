from django.db import models

# Create your models here.
class Subsystem(models.Model):
    subsys_name=models.CharField(max_length=500)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.subsys_name
    

class Document(models.Model):
    subsys=models.ForeignKey(Subsystem,on_delete=models.CASCADE)
    document_code=models.CharField(max_length=100)
    document_name=models.CharField(max_length=2000)
    document_version=models.CharField(max_length=10)
    document_format=models.CharField(max_length=50)
    document_status=models.BooleanField(default=False)
    document_base64_string=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.document_name
    

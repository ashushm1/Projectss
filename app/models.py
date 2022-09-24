from django.db import models
# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_hidden = models.BooleanField(default=False)
    
    def __str__(self):
        return '%s' % (self.name)
    
class Document(models.Model):
    CHOICES = (
        ('1', 'Aadhar Card'),
        ('2', 'PAN Card'),
        ('3', 'Driving Licence'),
        ('4', 'Other')
    )
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE, related_name='Folder')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    template_type = models.CharField(max_length=50, choices=CHOICES, default='4')
    
    def __str__(self):
        return '%s' % (self.name)
    
class File(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['file', str(instance.name), filename])
    
    document = models.ForeignKey('Document', on_delete=models.CASCADE, related_name='Document')
    file = models.FileField(upload_to=nameFile, blank=True, null=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content_type = models.CharField(max_length=50)
    #thumbnail = models
    
    def __str__(self):
        return '%s' % (self.name)
   
   
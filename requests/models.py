from django.db import models 
from django.contib.auth.models import User

class ServiceRequest(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('in_progess','In_Progesss'),
        ('resolved','Resolved'),
    ]
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    request_type=models.CharField(max_length=200)
    description=models.TextField()
    attachment=models.FileField(upload_to='attachments/',blank=True,null=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.request_type}- {self.customer.username}"

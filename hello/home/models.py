from django.db import models

# Create your models here.

class Contact(models.Model):
    email=models.CharField(max_length=122)
    name=models.CharField(max_length=122)
    TEXTBOX_CHOICES = (
        ('Missing/Broken/Wrong Item', 'Missing/Broken/Wrong Item'),
        ('Delayed Delivery', 'Delayed Delivery'),
        ('Exchange/Return Order', 'Exchange/Return Order'),
        ('Delivery Related Complaint', 'Delivery Related Complaint'),
        ('Other', 'Other'),
    )

    textbox = models.CharField(max_length=122, choices=TEXTBOX_CHOICES)
    other_details=models.TextField(max_length=122,blank=True,null=True)
    date=models.DateField()

    def __str__(self) :
        return self.email
    
# class SignUp(models.Model):
#     newEmail=models.CharField(max_length=50)
#     newPassword=models.CharField(max_length=122)
#     confirmPassword=models.CharField(max_length=122,default='newPassword')


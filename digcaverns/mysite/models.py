from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Contact(models.Model):
    """Model used to track contacts"""
    email = models.EmailField(unique=True, blank=False, 
                              null=False)
    first_name = models.CharField(max_length=30, blank=True, 
                                  null=False, default='')
    last_name = models.CharField(max_length=30, blank=True, 
                                 null=False, default='')

    def __str__(self) -> str:
        return f"{self.first_name} - {self.last_name}"


class ContactMessage(models.Model):
    """Model used to track contact messages"""

    contact = models.ForeignKey(to=Contact, 
                                on_delete=models.CASCADE, 
                                related_name='contact_event')
    contact_date = models.DateField(auto_now_add=True, 
                                    editable=False)
    content = models.TextField(max_length=280, blank=True, 
                               null=False, default='')
        
    class Status(models.TextChoices):
        """Track the status of the contacts"""

        NEW = "NEW", _("New"),
        OK = "OK", _("Ok")  # Seen and attended
        IGNORE = "IGN", _("Ignore"),  # Seen and don't care
    
    status = models.CharField(max_length=5, 
                              choices=Status.choices, 
                              default=Status.NEW)

    def __str__(self) -> str:
        return f"{self.status} - {self.contact}"

#models.py
from django.db import models
import uuid

# Create your models(class)(tabla) here.

#model formulario de contacto   
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_name    


#model de los flanes 
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True) #no necesario para este proyecto pero de gran utilidad para llevar registro de edicion de los productos
    update_at = models.DateTimeField(auto_now=True) #no necesario para este proyecto pero de gran utilidad para llevar registro de edicion de los productos
    
    
    def __str__(self) -> str:
        return f"objeto producto: {self.slug} - {self.is_private} - {self.name} "
    
 

    
    
    
    
    
    
    
    
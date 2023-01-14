from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

from .models import Customer


def customer_profil(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group) 
        
        Customer.objects.create(
			user=instance,
			name=instance.username,
				)
        
        print('user creation done')
        
post_save.connect(customer_profil, sender=User)        
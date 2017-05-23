from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Recipient(models.Model):
	user = models.ForeignKey(User)
	recipientname = models.CharField(max_length=200)
	recipientemail = models.EmailField()

	def __unicode__(self):
		return self.recipientname

	def get_all_emailbody(self):
		emailbody = EmailBody.objects.filter(recipient=self)
		return emailbody


class EmailBody(models.Model):
	recipient = models.ForeignKey(Recipient)
	emailbody = models.CharField(max_length=1024)
	created_date = models.DateTimeField(auto_now_add=True)	

	def __unicode__(self):
		return self.emailbody

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=30, blank=True, default='standupmeeting')
    role = models.CharField(max_length=30, blank=True, default='productmanager')
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()        	
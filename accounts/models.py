from django.db import models
from django.contrib.auth.models import User

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

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from dashboard.forms import RecipientForm, ComposeForm
from accounts.models import Recipient, EmailBody
from django.contrib.auth.models import User
from django.contrib import messages

def dashboard_home(request, template='dashboard/dashboard_home.html'):
	return render_to_response(template, context_instance=RequestContext(request))

def compose(request, template='dashboard/compose.html'):
	msg = []
	user = User.objects.get(username='sampath kumar')
	recipient = Recipient.objects.filter(user=user)
	recipient_list = []
	for r in recipient:
		recipient_list.append(r)

	if request.method == 'POST':
		form = ComposeForm(request.POST)
		if form.is_valid():
			emailbody = form.cleaned_data['emailbody']
			emailbody_content = request.POST.getlist('emailbody')
			for i in range(len(recipient_list)):
				re = EmailBody(recipient=recipient_list[i],emailbody=emailbody_content[i])
				re.save()
			messages.success(request, 'Emails shot !')	
			return HttpResponseRedirect('/dashboard/compose/')		
			
	else:
		form = ComposeForm()
	recipient = Recipient.objects.filter(user=user)	

	context = {
	'form':form,
	'msg':msg,
	'recipient':recipient,
	}			
	return render_to_response(template,context,context_instance=RequestContext(request))

def configure(request, template='dashboard/configure.html'):
	msg = []
	user = User.objects.get(username='sampath kumar')
	if request.method == 'POST':
		form = RecipientForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			recipient = Recipient(user=user, recipientname=name, recipientemail=email)
			recipient.save()
			messages.success(request, 'Recipient added !')
			return HttpResponseRedirect('/dashboard/configure/')
	else:
		form = RecipientForm()
	recipient = Recipient.objects.filter(user=user)
		

	context = {
	'form':form,
	'msg':msg,
	'recipient':recipient,
	}			
	return render_to_response(template,context,context_instance=RequestContext(request))

def log(request, template='dashboard/log.html'):
	user = User.objects.get(username='sampath kumar')
	recipient = Recipient.objects.filter(user=user)
	
			
	context = {
	'recipient':recipient,
	}

	return render_to_response(template,context,context_instance=RequestContext(request))

def monthly_summary(request, template='dashboard/log.html'):
	return render_to_response(template, context_instance=RequestContext(request))	


#main logics
#logic to send email

def send_mail():
	pass
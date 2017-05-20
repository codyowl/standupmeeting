from django.shortcuts import render, render_to_response
from django.template import RequestContext
from dashboard.forms import RecipientForm, ComposeForm

def dashboard_home(request, template='dashboard/dashboard_home.html'):
	return render_to_response(template, context_instance=RequestContext(request))

def compose(request, template='dashboard/compose.html'):
	msg = []
	if request.method == 'POST':
		form = ComposeForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']

	else:
		form = ComposeForm()

	context = {
	'form':form,
	'msg':msg,
	}			
	return render_to_response(template,context,context_instance=RequestContext(request))

def configure(request, template='dashboard/configure.html'):
	msg = []
	if request.method == 'POST':
		form = RecipientForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']

	else:
		form = RecipientForm()

	context = {
	'form':form,
	'msg':msg,
	}			
	return render_to_response(template,context,context_instance=RequestContext(request))

def log(request, template='dashboard/log.html'):
	return render_to_response(template, context_instance=RequestContext(request))

def monthly_summary(request, template='dashboard/log.html'):
	return render_to_response(template, context_instance=RequestContext(request))	

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from dashboard.forms import RecipientForm

def dashboard_home(request, template='dashboard/dashboard_home.html'):
	return render_to_response(template, context_instance=RequestContext(request))

def compose(request, template='dashboard/compose.html'):
	return render_to_response(template, context_instance=RequestContext(request))

def configure(request, template='dashboard/configure.html'):
	return render_to_response(template, context_instance=RequestContext(request))

def log(request, template='dashboard/log.html'):
	return render_to_response(template, context_instance=RequestContext(request))

def monthly_summary(request, template='dashboard/log.html'):
	return render_to_response(template, context_instance=RequestContext(request))	

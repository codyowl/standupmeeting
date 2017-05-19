from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from home.forms import LoginForm
from django.template import RequestContext


def home_login(request, template='home/home_login.html'):
	msg = []
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			driver = authenticate(username=username, password=password)
			if driver is not None:
				login(request, driver)
				return HttpResponseRedirect('/dashboard')
			else:
				msg.append("OOPS !! Invalid login details provided")
				return render_to_response(template, {'form': form, 'errors':msg}, context_instance=RequestContext(request))
		
		else:
			return render_to_response(template, {'form': form}, context_instance=RequestContext(request))
	else:
		form = LoginForm()
		context = {'form': form}
		return render_to_response(template, context, context_instance=RequestContext(request))
#from django.shortcuts import render, render_to_response
#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
	#return render_to_response('index.html')
	print(request.user),
	return render(request, 'index.html')
	#template = loader.get_template('index.html')
	#return HttpResponse(template.render({}, request))
	#return render('templates\index.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

class ProfileView(LoginRequiredMixin, TemplateView):
	template_name = 'accounts/profile.html'
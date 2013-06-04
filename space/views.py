# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import get_template
from space.forms import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

def index(request):   
  return render_to_response('index.html',context_instance=RequestContext(request))

def register(request):
    #注册提交
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])  
            new_user.save()  
            return render_to_response('index.html',context_instance=RequestContext(request))  
        else:  
            return render_to_response('registration/register.html', {'form':form})  
    #超链接点击过来的注册  
    else:  
        return render_to_response('registration/register.html',context_instance=RequestContext(request))    

        
def download_application_form(request):
    #file = open('..space.media.doc.application_form.doc').read()
    file = open('F:/DjangoPro/mysite/space/media/doc/application_form.doc').read()
    response = HttpResponse(file,mimetype='application/doc')
    response['Content-Disposition'] = 'attachment; filename=application_form.doc' 
    return response
        


def intro(request):
    return render_to_response('intro.html',context_instance=RequestContext(request))

def events(request):
    return render_to_response('events.html',context_instance=RequestContext(request))

def service(request):
    return render_to_response('service.html',context_instance=RequestContext(request))

def business_support(request):   
    return render_to_response('support.html',context_instance=RequestContext(request))

def about_us(request):
    return render_to_response('about_us.html',context_instance=RequestContext(request))

  
def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        message='You searched for: %r' %request.GET['q']
    else:
        message='You submitted an empty form.'
    return HttpResponse(message)
        
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        cd = form.clenaed_data
        send_email(
            cd['subject'],
            cd['message'],
            cd.get('email','noreply@example.com'),
            ['pusonchen@gmail.com'],
            )
        return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html',{'form':form})
    
    
# Create your views here.
from django.http import HttpResponse
import requests
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from facebook.settings import APP_ID, APP_SECRET, REDIRECT_URI
import json
import re
import facebook

access_token=[]

def login(request):
    
    login_url = "https://graph.facebook.com/oauth/authorize?client_id="+APP_ID+"&redirect_uri="+REDIRECT_URI
    data = { "login_url": login_url }
    return render_to_response("index.html",data,context_instance=RequestContext(request))    

def get_code(request):
    
    try:
        code = request.GET['code']
    except Exception:
        return HttpResponse (" Please press okay...")
        
    url = "https://graph.facebook.com/oauth/access_token?"
    pay_load = {"client_id":APP_ID, "client_secret": APP_SECRET, "redirect_uri": REDIRECT_URI, "code": code  }
    response = requests.post(url,pay_load)
    result = response.text 
    token = re.split(r'=',result)[1] # string split using regx
    access_token.insert(0,token)
    if access_token:
        return render_to_response("form.html",context_instance=RequestContext(request))       
    else:   
        return HttpResponse ("Invalid Access Token...")

def get_friends(request):
    #import pdb
    #pdb.set_trace()
    if access_token:
        url = "https://graph.facebook.com/me/friends?access_token="+access_token[0]
        response = requests.get(url)
        result = json.loads(response.text)
        data={'friends_count':len(result['data'])}
        return render_to_response("form.html",data,context_instance=RequestContext(request)) 
    else:
        return HttpResponse ("Invalid Access Token...")


def get_profile(request):
    
    #import pdb
    #pdb.set_trace()
    if access_token:
        url = "https://graph.facebook.com/me?access_token="+access_token[0]
        response = requests.get(url)
        result = json.loads(response.text)
        return render_to_response("form.html",result,context_instance=RequestContext(request)) 
    else:
        return HttpResponse ("Invalid Access Token...")

    
    
    

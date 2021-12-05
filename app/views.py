from django.shortcuts import render,HttpResponse,get_object_or_404
from .render import Render
from .models import Certificate
import re
import os
import mimetypes
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

 
def check(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
def pdf(request,id):
    first = get_object_or_404(Certificate,pk=id)
    # first = Certificate.objects.get(id=id)
    return Render.render(str(first.certificate_template.file), first)

def notfound(request,exception):
    return render(request,'404.html',{})

def notfound500(request):
    return render(request,'404.html',{})

def index(request):
    if request.method == 'POST':
        email = request.POST.get('id-or-email')
        if(check(email)):
            first = get_object_or_404(Certificate,email=email)
            return render(request,'pdf_page.html',{'data':first})
            # return  Render.render(str(first.certificate_template.file), first)
        first = get_object_or_404(Certificate,pk=email)
        return render(request,'pdf_page.html',{'data':first})
        # return Render.render(str(first.certificate_template.file), first)
    return render(request,'index.html',{})

def test(request):
    return render(request,'pdf_page.html',{})

def download_file(request):
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    filename = 'test.txt'
    
    filepath = BASE_DIR + '/downloadapp/Files/' + filename
    
    path = open(filepath, 'r')
   
    mime_type, _ = mimetypes.guess_type(filepath)
  
    response = HttpResponse(path, content_type=mime_type)
    
    response['Content-Disposition'] = "attachment; filename=%s" % filename
   
    return response
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from .models import Subsystem,Document
import datetime
from django.contrib import messages

# Create your views here.
def home(request):

    context={

    }

    return render(request,"docmanage/doclist.html",context)

def subsystem_list(request):
    sublist=Subsystem.objects.all()
    context={
        "sublist":sublist,
    }

    return render(request,"docmanage/subsyslist.html",context)

def document_list(request):
    context={

    }

    return render(request,"docmanage/doclist.html",context)

def subsys_create(request):
    if request.method=='POST':
        data=request.POST
        context={

        }
        subsys=Subsystem.objects.create(
            subsys_name=data['subsys_name']
        )

        return redirect('home')
    return render(request,"docmanage/subsyscreate.html",context)

def document_create(request):
    if request.method=='POST':
        data=request.POST
        doc=Document.objects.create(
            document_code=data['document_code'],
            document_name=data['document_name'],
            document_version=data['document_version'],
            document_format=data['document_format'],
            document_status=data['document_status'],
            document_base64_string=data['document_base64_string'],
        )

        context={

        }

        return redirect('home')
    return render(request,"docmanage/doccreate.html",context)

def subsystem_detail(request, subsys_id):
    subsys = get_object_or_404(Subsystem, pk=subsys_id)
    context={
        "subsys":subsys,
    }
    return render(request,"docmanage/subsystemdetail.html",context)

def subsystem_update(request,subsys_id):
    subsys = get_object_or_404(Subsystem, pk=subsys_id)
    if request.method=='POST':
        Subsystem.objects.filter(id = id).update(
            subsys_name=request.POST.get("subsys_name"),
            modified_date=datetime.datetime.now()
        )
        context={
            'subsys':subsys,
        }
        return render(request,"docmanage/subsystemdetail.html",context) 
    # return HttpResponse(template.render(context,request))

def document_detail(request, document_id):
    return HttpResponse("This is document detail %s" % document_id)

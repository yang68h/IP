from django.shortcuts import render
from forms import *
from models import HostIp
from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator

# Create your views here.
def Recodeip(request):
    if request.method == 'POST':
        repo=HostAddr(request.POST)
        if repo.is_valid():
            info=HostIp()

            info.mac=repo.cleaned_data['hostMac']
            info.user=repo.cleaned_data['hostUser']
            info.ipaddr=repo.cleaned_data['hostIpaddr']
            info.save()
            return HttpResponseRedirect('/')
    else:
        repo=HostAddr()
    return  render(request,'ip.html',{'form':repo})
def SelfPaginator(request, List, Limit):
    paginator = Paginator(List, int(Limit))
    page = request.GET.get('page')
    try:
        lst = paginator.page(page)
    except PageNotAnInteger:
        lst = paginator.page(1)
    except EmptyPage:
        lst = paginator.page(paginator.num_pages)
    return lst

def listip(request):
    allip=HostIp.objects.all()
    lip = SelfPaginator(request,allip,20)
    kwvars = {
        'lpage':lip,
        'request':request,
    }
    return render_to_response('list.html',kwvars)



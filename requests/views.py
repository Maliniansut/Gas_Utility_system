from django.shortcuts import render,redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required

def create_request(request):
    if request.method=='POST':
        form = ServiceRequestForm(request.POST,request.FILES)
        if form.is_valid():
            service_request=form.save(commit=False)
            service_request.customer=request.user
            service_request.save()
            return redirect('request_list')
    else:
        form =ServiceRequestForm()
    return render(request,'requests/create_request.html',{'form':form})

def request_list(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request,'requests/request_list.html',{'requests':requests})
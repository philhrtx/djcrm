from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request,"lead_list.html", context=context)

#pk stand for primary key
def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "lead_detail.html", context=context)
from re import M
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm

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

def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            return redirect("/leads")
             
    context = {
        "form": LeadForm()
    }
    return render(request, "lead_create.html", context)
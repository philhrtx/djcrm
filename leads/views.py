from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic

from .models import Lead, Agent
from .forms import LeadModelForm

# CRUD+L = Create Retrieve Update Delete + list

class LandingPageView(generic.TemplateView):
 template_name = "landing.html"


def landing_page(request):
    return render(request,"landing.html")

class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request,"leads/lead_list.html", context=context)

#pk stand for primary key
def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context=context)

class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
             
    context = {
        "form": LeadModelForm()
    }
    return render(request, "leads/lead_create.html", context)

class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-list") 

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(request.POST, instance=lead)
    if form.is_valid():
            form.save()
            return redirect("/leads")        
    context = {
        "form": form,
        "lead": lead,
    } 
    return render(request, "leads/lead_update.html", context)

class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse("leads:lead-list") 

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    def get_success_url(self):
        return reverse("leads:lead-list") 
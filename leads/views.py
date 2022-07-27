from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView , DetailView, CreateView, UpdateView, DeleteView      
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm




class SignupView(CreateView):
   template_name = "registration/signup.html"
   form_class = CustomUserCreationForm

   def get_success_url(self):
       return reverse("login")


def landing_page(request):
   return render(request, "landing.html")


class LeadListView(LoginRequiredMixin,ListView):
   template_name = "leads/leads_list.html"
   queryset = Lead.objects.all()
   context_object_name = "leads"

# Create your views here.
def leads_list(request):
    #return HttpResponse("Hello world")
    leads = Lead.objects.all()
    context =  {
       "leads": leads
    }
    return render(request, "leads/leads_list.html",context)


class LeadDetailView(LoginRequiredMixin, DetailView):
   template_name = "leads/lead_details.html"
   queryset = Lead.objects.all()
   context_object_name = "lead"

def load_detail(request, pk):

   lead = Lead.objects.get(id=pk)
   context = {
      "lead": lead
   }
   return render(request, "leads/lead_details.html", context)


class LeadCreateView(LoginRequiredMixin, CreateView):
   template_name = "leads/lead_create.html"
   form_class = LeadModelForm
   def get_success_url(self):
       return reverse("leads:lead-list")

   def form_valid(self, form):
      send_mail(
         subject="Lead has been created", message="Go to the site ", from_email="test@test.com", recipient_list=["edgarse1945@gmail.com"]
      )
      return super(LeadCreateView, self).form_valid(form)

def lead_create(request):
   form = LeadModelForm()

   if request.method  == "POST":
      print("POST jeje")
      form = LeadModelForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("/leads")
   context = {
      "form": form
   }
   return render(request, "leads/lead_create.html", context)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
   template_name = "leads/lead_update.html"
   form_class = LeadModelForm
   queryset = Lead.objects.all()
   def get_success_url(self):
       return reverse("leads:lead-list")


def lead_updtae(request, pk):
   
   lead = Lead.objects.get(id=pk)
   form = LeadModelForm(instance=lead)

   if request.method  == "POST":
      print("POST jeje")
      form = LeadModelForm(request.POST, instance=lead)
      if form.is_valid():
         form.save()
         return redirect("/leads")
   context = {
      "form": form,
      "lead": lead
   }
   return render(request, "leads/lead_delete.html", context)


class LeadDeleteView(LoginRequiredMixin, DeleteView):
   template_name = "leads/lead_delete.html"
   queryset = Lead.objects.all()
   def get_success_url(self):
       return reverse("leads:lead-list")

def lead_delete(request, pk):
   lead = Lead.objects.get(id=pk)
   lead.delete()
   return redirect("/leads")


# def lead_updtae(request, pk):
#    lead = Lead.objects.get(id=pk)
#    form = LeadForm()

#    if request.method  == "POST":
#       form = LeadForm(request.POST)
#       if form.is_valid():
#          first_name = form.cleaned_data["first_name"]
#          last_name = form.cleaned_data["last_name"]
#          age = form.cleaned_data["age"]
#          # agent = form.cleaned_data["agent"]
         
#          lead.first_name = first_name
#          lead.last_name = last_name
#          lead.age = age

#          lead.save()
#          return redirect("/leads")
#    context = {
#       "form": form,
#       "lead": lead
#    }

#    return render(request, "leads/lead_update.html", context)


# def lead_create_v2(request):
#    form = LeadModelForm()

#    if request.method  == "POST":
#       print("POST jeje")
#       form = LeadModelForm(request.POST)
#       if form.is_valid():
#          first_name = form.cleaned_data["first_name"]
#          last_name = form.cleaned_data["last_name"]
#          age = form.cleaned_data["age"]
#          agent = form.cleaned_data["agent"]
         
#          lead = Lead.objects.create(
#             first_name=first_name,
#             last_name=last_name,
#             age=age,
#             agent=agent
#          )
     
#          return redirect("/leads")
#    context = {
#       "form": form
#    }
#    return render(request, "leads/lead_create.html", context)
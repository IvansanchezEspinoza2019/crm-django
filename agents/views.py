import random
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.urls import reverse
from agents.forms import AgentModelForm
from .mixins import OrganizerAndLoginRequiredMixin
from django.core.mail import send_mail

class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    template_name= "agents/agent_list.html"
    def get_queryset(self):
        request_user_org = self.request.user.userprofilemodel
        return Agent.objects.filter(organization=request_user_org)

class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name= "agents/create_agent.html"
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Agent.objects.create(user=user, organization=self.request.user.userprofilemodel)
        send_mail(
            subject="You are invited to be an agent",
            message="You were added as an agent on DJCRM, Please come login to start working.",
            from_email="admin@test.com",
            recipient_list=[user.email]
        )
        #agent.organization = self.request.user.userprofilemodel
        #agent.save()
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name= "agent"

    def get_queryset(self):
        request_user_org = self.request.user.userprofilemodel
        return Agent.objects.filter(organization=request_user_org)


class AgentUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name= "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")
    
    def get_queryset(self):
        request_user_org = self.request.user.userprofilemodel
        return Agent.objects.filter(organization=request_user_org) 

class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name= "agent"

    def get_queryset(self):
        request_user_org = self.request.user.userprofilemodel
        return Agent.objects.filter(organization=request_user_org) 

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")
from sre_constants import LITERAL_LOC_IGNORE
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.urls import reverse
from agents.forms import AgentModelForm

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name= "agents/agent_list.html"
    def get_queryset(self):
        request_user_org = self.request.user.userprofilemodel
        return Agent.objects.filter(organization=request_user_org)

class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name= "agents/create_agent.html"
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofilemodel
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name= "agent"

    def get_queryset(self):
        return Agent.objects.all() 


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name= "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")
    
    def get_queryset(self):
        return Agent.objects.all() 

class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name= "agent"

    def get_queryset(self):
        return Agent.objects.all() 

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")
from dataclasses import field
from django import forms
from django.contrib.auth import get_user_model
from .models import Lead, Agent
from django.contrib.auth.forms import UserCreationForm, UsernameField

# retrieves the our custom user model
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent'
        )

class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)

class AssignAgentForm(forms.Form):
    agents = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwards):
        request = kwards.pop("request")
        agents = Agent.objects.filter(organization=request.user.userprofilemodel)
        super(AssignAgentForm,self).__init__(*args, **kwards)
        self.fields["agents"].queryset = agents
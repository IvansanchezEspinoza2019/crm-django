from django.urls import path
from .views import leads_list, load_detail, lead_create, lead_updtae, lead_delete

app_name = 'leads'

urlpatterns = [
    path('', leads_list, name='lead-list'),
    path('create/', lead_create,  name='lead-create'),
    path('<int:pk>/', load_detail,  name='lead-detail'),
    path('<int:pk>/update/', lead_updtae, name='lead-update'),
    path('<int:pk>/delete/', lead_delete, name='lead-delete')
]
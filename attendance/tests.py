from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from . import views
factory = APIRequestFactory()
user = User.objects.get(username='Batu')
view = views.WorkersListView.as_view()

# Make an authenticated request to the view...
request = factory.get('/workers/')
force_authenticate(request, user=user)
response = view(request)
print(response)

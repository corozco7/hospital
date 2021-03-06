from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('hospital.users.urls.login', 'login'), namespace='login')),
    path('', include(('hospital.appointment.urls.clients', 'clients'), namespace='clients')),
    path('doctors/', include(('hospital.appointment.urls.doctors', 'doctors'), namespace='doctors')),
    path('patients/', include(('hospital.appointment.urls.patients', 'patients'), namespace='patients'))
]

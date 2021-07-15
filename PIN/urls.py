from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('', include('PIN.core.urls', namespace='core')),
    path('accounts/', include('PIN.accounts.urls')),  # without namespace
    path('category/', include('PIN.category.urls', namespace='category')),
    path('item/', include('PIN.item.urls', namespace='item')),
    # path('crm/', include('PIN.crm.urls', namespace='crm')),
    path('admin/', admin.site.urls),
]


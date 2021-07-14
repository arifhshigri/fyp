from django.urls import path

from PIN.item import views as v

app_name = 'item'


urlpatterns = [
    # path('', v.item_list, name='item_list'),
    # path('<int:pk>/', v.item_detail, name='item_detail'),
    # path('create/', v.item_create, name='item_create'),
    # path('<int:pk>/update/', v.item_update, name='item_update'),
    # path('<int:pk>/delete/', v.item_delete, name='item_delete'),
    path('', v.itemListView.as_view(), name='item_list'),
    path('<int:pk>/', v.itemDetailView.as_view(), name='item_detail'),
    path('create/', v.itemCreateView.as_view(), name='item_create'),
    path('<int:pk>/update/', v.itemUpdateView.as_view(), name='item_update'),
    path('<int:pk>/delete/', v.itemDeleteView.as_view(), name='item_delete'),
]

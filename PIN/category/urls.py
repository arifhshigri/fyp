from django.urls import path

from PIN.category import views as v

app_name = 'category'


urlpatterns = [
    # path('', v.category_list, name='category_list'),
    # path('<int:pk>/', v.category_detail, name='category_detail'),
    # path('create/', v.category_create, name='category_create'),
    # path('<int:pk>/update/', v.category_update, name='category_update'),
    # path('<int:pk>/delete/', v.category_delete, name='category_delete'),
    path('', v.categoryListView.as_view(), name='category_list'),
    path('<int:pk>/', v.categoryDetailView.as_view(), name='category_detail'),
    path('create/', v.categoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/update/', v.categoryUpdateView.as_view(), name='category_update'),
    path('<int:pk>/delete/', v.categoryDeleteView.as_view(), name='category_delete'),
]

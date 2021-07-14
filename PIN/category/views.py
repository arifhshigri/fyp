from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from .forms import CategoryForm
from .models import Category


def category_list(request):
    template_name = 'category/category_list.html'
    object_list = Category.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def category_detail(request, pk):
    template_name = 'category/category_detail.html'
    obj = Category.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def category_create(request):
    template_name = 'category/category_form.html'
    form = CategoryForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('category:category_list')

    context = {'form': form}
    return render(request, template_name, context)


def category_update(request, pk):
    template_name = 'category/category_form.html'
    instance = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('category:category_list')

    context = {'form': form}
    return render(request, template_name, context)


def category_delete(request, pk):
    template_name = 'category/category_confirm_delete.html'
    obj = Category.objects.get(pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('category:category_list')

    context = {'object': obj}
    return render(request, template_name, context)


class categoryListView(ListView):
    model = Category
    paginate_by = 10


class categoryDetailView(DetailView):
    model = Category
    paginate_by = 10


class categoryCreateView(CreateView):
    model = Category
    paginate_by = 10
    form_class = CategoryForm


class categoryUpdateView(UpdateView):
    model = Category
    paginate_by = 10
    form_class = CategoryForm


class categoryDeleteView(DeleteView):
    model = Category
    paginate_by = 10
    success_url = reverse_lazy('category:category_list')

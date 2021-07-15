from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from .forms import ItemForm
from .models import Item


def item_list(request):
    template_name = 'item/item_list.html'
    object_list = Item.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def item_detail(request, pk):
    template_name = 'item/item_detail.html'
    obj = Item.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def item_create(request):
    template_name = 'item/item_form.html'
    form = ItemForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('item:item_list')

    context = {'form': form}
    return render(request, template_name, context)


def item_update(request, pk):
    template_name = 'item/item_form.html'
    instance = Item.objects.get(pk=pk)
    form = ItemForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('item:item_list')

    context = {'form': form}
    return render(request, template_name, context)


def item_delete(request, pk):
    template_name = 'item/item_confirm_delete.html'
    obj = Item.objects.get(pk=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('item:item_list')

    context = {'object': obj}
    return render(request, template_name, context)


class itemListView(ListView):
    model = Item
    paginate_by = 10


class itemDetailView(DetailView):
    model = Item
    paginate_by = 10


class itemCreateView(CreateView):
    model = Item
    paginate_by = 10
    form_class = ItemForm


class itemUpdateView(UpdateView):
    model = Item
    paginate_by = 10
    form_class = ItemForm


class itemDeleteView(DeleteView):
    model = Item
    paginate_by = 10
    success_url = reverse_lazy('item:item_list')

from django import forms

from .models import Item
from .widgets import BootstrapDateTimePickerInput


class ItemForm(forms.ModelForm):
    required_css_class = 'required'
    bid_start_date = forms.DateTimeField(
        # input_formats=['%m/%d/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput()
    )
    bid_end_date = forms.DateTimeField(
        # input_formats=['%m/%d/%Y %H:%M:%S'],
        widget=BootstrapDateTimePickerInput()
    )

    class Meta:
        model = Item
        # fields = '__all__'
        fields = (
            'title',
            'description',
            'base_price',
            'sold_price',

            'category',
            'status',
            'active',
        )

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['active'].widget.attrs['class'] = None

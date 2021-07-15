from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Category
        # fields = '__all__'
        fields = (
            'cat_name',
            'active',
        )

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['active'].widget.attrs['class'] = None



from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        # widgets = {
        #     'field1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'field2': forms.EmailInput(attrs={'class': 'form-control'}),
        # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.label = ''
    #         field.widget.attrs.update({'placeholder': f'Enter {field.label}'})
    #

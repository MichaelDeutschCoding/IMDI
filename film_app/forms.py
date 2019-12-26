from django.forms import ModelForm, TextInput, Select, CheckboxSelectMultiple, DateInput, NumberInput, FileInput
from film_app.models import Film, Director
from django.forms.widgets import Textarea

class AddFilmForm(ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': "form-control w-75", }),
            'country': Select(attrs={'class': "form-control w-75", }),
            'director': Select(attrs={'class': "form-control w-75", }),
            'category': CheckboxSelectMultiple(attrs={'class': "form",}),
            'release_date': DateInput(attrs={'type': 'date', 'class': 'form-control w-75',}),
            'rating': NumberInput(attrs={'type': 'range',
                                         'step': '1',
                                         'min': '1',
                                         'max': '10',
                                         'class': 'form-control w-75',
                                         'oninput': 'updateTextInput(this.value)',
                                         }),
            'image': FileInput(attrs={'class': "form-control-file w-75",}),
            'about': Textarea(attrs={'class': 'form-control w-75'}),
        }


class AddDirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

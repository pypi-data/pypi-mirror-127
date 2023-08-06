## django-json-model-widget

Django widget for storing model instances pairs in flat JsonField.

### Install stable version from PyPI

Install from PyPI:

```
pip install django-flat-json-widget
```

### Usage

Add flat_json_widget to INSTALLED_APPS:

```python
INSTALLED_APPS = [
    # other apps...
    'json_model_widget',
]
```

Then load the widget where you need it, for example, here's how to use it in the django admin site:

```python
from django import forms
from json_model_widget.widgets import JsonPairInputs
from .models import model1, model2


class MyForm(forms.ModelForm):
    class Meta:
        widgets = {
            'fieldname': JsonPairInputs(model1, model2)
        }
```

### Contributors

Oleg Galichkin <galij899@yandex.ru>

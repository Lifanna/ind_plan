import unicodedata
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .._models import org_method_work_models as models
from translated_fields.utils import language_code_formfield_callback


class DateInput(forms.DateInput):
    input_type = 'date'


class InternationalCooperationWorkForm(forms.ModelForm):
    form_field_callback = language_code_formfield_callback

    # def clean(self):
        # username = self.cleaned_data.get('username')

        # return self.cleaned_data

    class Meta:
        model = models.OrgMethodWork
        fields = '__all__'
        exclude = (
            'user',
        )
        error_messages = {
            'org_method_work_type': {
                'required': "Пожалуйста, укажите вид учебно-методической работы"
            },
        }


class CategoryChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
        return "OrgMethodWorkType: {}".format(obj.name)

import unicodedata
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .._models import edu_method_work_models as models
from translated_fields.utils import language_code_formfield_callback


class EduMethodWorkForm(forms.ModelForm):
    form_field_callback = language_code_formfield_callback
    # def clean(self):
        # username = self.cleaned_data.get('username')

        # return self.cleaned_data

    class Meta:
        model = models.EduMethodWork
        fields = '__all__'
        exclude = (
            'user',
        )
        error_messages = {
            'education_work_type': {
                'required': "Пожалуйста, укажите вид учебной работы"
            },
            'by_plan_1': {
                'required': "Пожалуйста, введите план 1 семестр"
            },
            'by_fact_1': {
                'required': "Пожалуйста, введите факт 1 семестр"
            },
            'deviation_1': {
                'required': "Пожалуйста, введите отклонение 1 семестр"
            },
            'by_plan_2': {
                'required': "Пожалуйста, введите план 2 семестр"
            },
            'by_fact_2': {
                'required': "Пожалуйста, введите факт 2 семестр"
            },
            'deviation_2': {
                'required': "Пожалуйста, введите отклонение 2 семестр"
            },
            'by_plan_annual': {
                'required': "Пожалуйста, введите план годовой"
            },
            'by_fact_annual': {
                'required': "Пожалуйста, введите факт годовой"
            },
            'deviation_annual': {
                'required': "Пожалуйста, введите отклонение годовой"
            },
        }


class CategoryChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
        return "EduMethodWorkType: {}".format(obj.name)
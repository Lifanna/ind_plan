import unicodedata
from django import forms
from . import models


class EducationalWorkForm(forms.ModelForm):
    # def clean(self):
        # username = self.cleaned_data.get('username')

        # return self.cleaned_data

    class Meta:
        model = models.EducationalWork
        fields = '__all__'
        # error_messages = {
            # 'password': {
            #     'required': "Пожалуйста, введите пароль"
            # }
        # }


class CategoryChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
        return "EducationWorkType: {}".format(obj.name)
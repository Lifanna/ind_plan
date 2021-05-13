import os
from django.core.exceptions import ValidationError


def upload_to(instance, filename):
    print('USER and RECORD ID', instance.user.id, instance.pk)
    return os.path.join("uploads/" + str(instance.user.id) + "/" + str(instance.id), filename)

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.rar',]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Неподдерживаемый тип расширения файла')

# -*- coding: utf-8 -*-
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from .models import User
import logging


LOGGER = logging.getLogger(__name__)

class CustomBackend(ModelBackend):
    """
    Аутентификация пользователя может происходить через login
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        # print("зашел", username, password)
        User = get_user_model()
        # if username is None:
        #     username = kwargs.get(User.USERNAME_FIELD)
        if username is None or password is None:
            return
        if not isinstance(username, str):
            return
        
        # check that username doesn't have spaces
        username = username.lstrip().rstrip().replace(' ', '')

        # phone_number = ''.join([ i for i in username if i.isdigit() ])

        allow = False
        try:
            user = User.objects.get(login__iexact=username)
        except User.DoesNotExist:
            return
        else:
            allow = check_password(password, user.password)
            LOGGER.info(f"Найден пользователь по username - {username}")

        if self.user_can_authenticate(user):
            print("иииииииии:                   ", user)
            # once the user was logged in, we update all his information
            return user

        return

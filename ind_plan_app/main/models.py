from django.db import models
from django.contrib.auth.models import AbstractUser, User, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, login, password, **extra_fields):
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, login, password=None, **extra_fields):
        """Создание нового пользователя по login и password"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login, password, **extra_fields)

    def create_superuser(self, login, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        print("ВВВВВВВВВвотттттттт:      ")
        print(login, password)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(login, password, **extra_fields)

    def is_unique_login(self, user):
        if user.id is not None and user.login != "" and self.filter(login=user.login).exclude(pk=user.pk).exists():
            return False
        return True


# ученое звание
class AcademicRank(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ученое звание'
        verbose_name_plural = 'Ученые звания'


# ученая степень
class AcademicDegree(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ученая степень'
        verbose_name_plural = 'Ученые степени'    


# должность
class Status(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


# ставка
class Rate(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ставка'
        verbose_name_plural = 'Ставки'


# форма занятости: штатный/совместитель
class BusinessForm(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Форма занятости'
        verbose_name_plural = 'Формы занятости'


# кафедра
class Chair(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Форма занятости'
        verbose_name_plural = 'Формы занятости'


# факультет
class Faculty(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Форма занятости'
        verbose_name_plural = 'Формы занятости'


class User(AbstractUser):
    username = None
    
    email = models.EmailField(('Email address'), blank=True)
    
    login = models.CharField("Login", unique=True, max_length=300)
    
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)

    patronymic = models.CharField("Patronymic", max_length=300)
    
    academic_degree = models.ForeignKey(AcademicDegree, on_delete=models.SET_NULL, null=True)
    
    academic_rank = models.ForeignKey(AcademicRank, on_delete=models.SET_NULL, null=True)

    chair = models.ForeignKey(Chair, on_delete=models.SET_NULL, null=True)

    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)

    rate = models.ForeignKey(Rate, on_delete=models.SET_NULL, null=True)

    business_form = models.ForeignKey(BusinessForm, on_delete=models.SET_NULL, null=True)
    
    USERNAME_FIELD = 'login'


    is_deleted = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        db_table = "auth_user"
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def clean(self):
        # here we can check some mandatory fields and complex relations between fields
        super(User, self).clean()

    def save(self, *args, **kwargs):
        print("DDDDDDDDDAAAAAAAAAAAAAAAAAAAA")
        self.clean()
        self.validate_unique()
        super(User, self).save(*args, **kwargs)

    def validate_unique(self, *args, **kwargs):
        super(User, self).validate_unique(*args, **kwargs)
        if not User.objects.is_unique_login(self):
            raise ValidationError("Пользователь уже существует")


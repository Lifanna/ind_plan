from django.db import models
from django.contrib.auth.models import AbstractUser, User, BaseUserManager
from django.utils.translation import gettext as _


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
        verbose_name = _('Academic rank')
        verbose_name_plural = _('Academic ranks')


# ученая степень
class AcademicDegree(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Academic degree')
        verbose_name_plural = _('Academic degrees')


# должность
class Status(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')


# ставка
class Rate(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Rate')
        verbose_name_plural = _('Rates')


# форма занятости: штатный/совместитель
class BusinessForm(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Business form')
        verbose_name_plural = _('Business forms')


# кафедра
class Chair(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Chair')
        verbose_name_plural = _('Chairs')


# факультет
class Faculty(models.Model):
    name = models.CharField(max_length=50, blank=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculties')


class User(AbstractUser):
    username = None
    
    email = models.EmailField(_('Email address'), blank=True)
    
    login = models.CharField(_('Login'), unique=True, max_length=300)
    
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, verbose_name=_('Status'), null=True)

    patronymic = models.CharField(_("Patronymic"), max_length=300)
    
    academic_degree = models.ForeignKey(AcademicDegree, verbose_name=_('Academic degree'), on_delete=models.SET_NULL, null=True)
    
    academic_rank = models.ForeignKey(AcademicRank, verbose_name=_('Academic rank'), on_delete=models.SET_NULL, null=True)

    chair = models.ForeignKey(Chair, on_delete=models.SET_NULL, verbose_name=_('Chair'), null=True)

    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, verbose_name=_('Faculty'), null=True)

    rate = models.ForeignKey(Rate, on_delete=models.SET_NULL, verbose_name=_('Rate'), null=True)

    business_form = models.ForeignKey(BusinessForm, on_delete=models.SET_NULL, verbose_name=_('Business form'), null=True)
    
    USERNAME_FIELD = 'login'

    is_deleted = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        db_table = "auth_user"
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def clean(self):
        # here we can check some mandatory fields and complex relations between fields
        super(User, self).clean()

    def save(self, *args, **kwargs):
        self.clean()
        self.validate_unique()
        super(User, self).save(*args, **kwargs)

    def validate_unique(self, *args, **kwargs):
        super(User, self).validate_unique(*args, **kwargs)
        if not User.objects.is_unique_login(self):
            raise ValidationError_("User is already exists")


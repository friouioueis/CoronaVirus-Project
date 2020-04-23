from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from rest_framework.authtoken.models import Token

ROLE_CHOICES = (
    ('si', 'simple'),
    ('rd', 'redacteur'),
    ('md', 'moderateur'),
    ('ad', 'admin')
)



class UtilisateurManager(BaseUserManager):
    def create(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):

        user = self.create(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class compteUtilisateur(AbstractBaseUser,PermissionsMixin):
    id                              = models.AutoField(primary_key=True, editable=False)
    username                        = models.CharField(max_length=30, unique=True, verbose_name="Nom d'utilisateur")
    email                           = models.EmailField(max_length=254, unique=True)
    date_joined				        = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				        = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				        = models.BooleanField(default=False)
    is_active				        = models.BooleanField(default=True)
    is_staff				        = models.BooleanField(default=False)
    is_superuser			        = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UtilisateurManager()

    @property
    def roles(self):
        return self.role_set.all()

    @property
    def infos(self):
        return self.infopersonel

    def __str__(self):
        return self.email + ': ' + self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class role(models.Model):
    idRole                          = models.AutoField(primary_key=True, editable=False)
    idUtilisateurR                  = models.ForeignKey(compteUtilisateur, on_delete=models.CASCADE, verbose_name='utilisateur')
    Type                            = models.CharField(max_length=2, choices=ROLE_CHOICES)

    def __str__(self):
        return self.get_Type_display() + ':' + self.idUtilisateurR.username


    def addRole(idUtilisateurR,Type):
        group = Group.objects.get(name=Type)
        user=compteUtilisateur.objects.get(id=idUtilisateurR)
        user.groups.add(group)

    def deleteRole(idUtilisateurR,Type):
        group = Group.objects.get(name=Type)
        user = idUtilisateurR
        group.user_set.remove(user)

class infoPersonel(models.Model):
    idInfoPer                       = models.AutoField(primary_key=True, editable=False)
    idUtilisateurIp                 = models.OneToOneField(compteUtilisateur, on_delete=models.CASCADE, verbose_name='utilisateur')
    nom                             = models.CharField(max_length=50, null=True)
    prenom                          = models.CharField(max_length=50, null=True)
    dateNaissance                   = models.DateField(verbose_name='Date de naissance', null=True)
    wilaya                          = models.CharField(max_length=30, null=True)

    class Meta:
        verbose_name_plural = 'Infos Personnelles'
    def __str__(self):
        return 'Infos de: ' + self.idUtilisateurIp.username

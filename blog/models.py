# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogappContact(models.Model):
    email = models.CharField(max_length=254)
    numero = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'blogApp_contact'


class BlogappGallery(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.CharField(max_length=100)
    date_posted = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blogApp_gallery'


class BlogappMessage(models.Model):
    nome = models.CharField(max_length=120)
    email = models.CharField(max_length=254)
    mensagem = models.TextField()

    class Meta:
        managed = False
        db_table = 'blogApp_message'


class BlogappPost(models.Model):
    titulo = models.CharField(max_length=100)
    abstracto = models.TextField()
    date_posted = models.DateTimeField()
    imagem = models.CharField(max_length=100)
    referencia = models.CharField(max_length=500)
    ficheiro = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'blogApp_post'    


class BlogappProfile(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    frase_do_dia = models.TextField()
    imagem = models.ImageField(default='static/img/author_image.png', upload_to='profile_pics')
    imagem_bio = models.ImageField(upload_to='profile_pics/bio_pics')
    
    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'blogApp_profile'


class BlogContact(models.Model):
    email = models.EmailField()
    numero = models.CharField(max_length=100)
    def __str__(self):
        return self.email

    class Meta:
        managed = False
        db_table = 'blog_contact'


class BlogGallery(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='gallery_pics') 
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.titulo

    class Meta:
        managed = False
        db_table = 'blog_gallery'


class BlogMessage(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    mensagem = models.TextField()
    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'blog_message'


class BlogPost(models.Model):
    titulo = models.CharField(max_length=100)
    abstracto = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    imagem = models.ImageField(upload_to='post_pics')
    referencia = models.URLField(default='none.com', max_length=500)
    ficheiro = models.FileField(default='none', upload_to='documents')
    def __str__(self):
        return self.titulo  

    class Meta:
        managed = False
        db_table = 'blog_post'
    def save(self):
        super().save()
        img = Image.open(self.imagem.path)
        
        if img.height > 800 or img.width > 500:
            img = img.resize((750, 500), Image.ANTIALIAS)   
            img.save(self.imagem.path)

class BlogProject(models.Model):
    titulo = models.CharField(max_length=100)
    abstracto = models.TextField()
    imagem = models.ImageField(upload_to='post_pics')
    referencia = models.URLField(default='none.com', max_length=500)
   
    def __str__(self):
        return self.titulo  

class BlogProfile(models.Model):
    biografia = models.TextField()
    frase_do_dia = models.TextField()
    imagem = models.CharField(max_length=100)
    imagem_bio = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'blog_profile'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

# Generated by Django 5.0.4 on 2024-05-08 07:00

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id_recurso', models.AutoField(primary_key=True, serialize=False)),
                ('solicitudes_encoladas', models.IntegerField()),
                ('tamano_ram', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('ubicacion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id_especialidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoPersona',
            fields=[
                ('id_estado_persona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id_facultad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id_recurso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='datacore.recurso')),
                ('nombre', models.CharField(max_length=200)),
                ('numero_nucleos_cpu', models.IntegerField()),
                ('frecuencia_cpu', models.DecimalField(decimal_places=6, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id_recurso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='datacore.recurso')),
                ('nombre', models.CharField(max_length=200)),
                ('numero_nucleos_gpu', models.IntegerField()),
                ('tamano_vram', models.IntegerField()),
                ('frecuencia_gpu', models.DecimalField(decimal_places=6, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('motivo_desautorizado', models.TextField(blank=True)),
                ('recursos_max', models.PositiveIntegerField(default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('id_especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datacore.especialidad')),
                ('id_estado_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datacore.estadopersona')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='especialidad',
            name='id_facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datacore.facultad'),
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_solicitud', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField()),
                ('estado_solicitud', models.CharField(max_length=100)),
                ('posicion_cola', models.IntegerField()),
                ('fecha_finalizada', models.DateTimeField()),
                ('parametros_ejecucion', models.TextField()),
                ('fecha_procesamiento', models.DateTimeField()),
                ('id_recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datacore.recurso')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
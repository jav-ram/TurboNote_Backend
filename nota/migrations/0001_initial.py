# Generated by Django 2.1.2 on 2018-10-16 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cuaderno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amistad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amigo1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friends', to=settings.AUTH_USER_MODEL)),
                ('amigo2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_unused_friend_relation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Compartido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compartido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='share_to', to=settings.AUTH_USER_MODEL)),
                ('dueno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.TextField(blank=True, null=True)),
                ('pertenece', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuaderno.Cuaderno')),
            ],
        ),
        migrations.AddField(
            model_name='compartido',
            name='nota',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note', to='nota.Nota'),
        ),
    ]

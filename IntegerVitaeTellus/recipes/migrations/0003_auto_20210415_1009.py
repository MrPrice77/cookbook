# Generated by Django 3.2 on 2021-04-15 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_auto_20210414_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('ingredients', models.CharField(blank=True, max_length=500, null=True)),
                ('instructions', models.CharField(blank=True, max_length=1000, null=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Recipes',
        ),
    ]

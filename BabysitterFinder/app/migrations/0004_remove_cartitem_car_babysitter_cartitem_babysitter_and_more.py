# Generated by Django 5.0 on 2023-12-11 01:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cartitem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='car',
        ),
        migrations.CreateModel(
            name='Babysitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='babysitter_images')),
                ('is_booked', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cartitem',
            name='babysitter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.babysitter'),
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]

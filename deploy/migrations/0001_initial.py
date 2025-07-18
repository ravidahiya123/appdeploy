# Generated by Django 5.2.3 on 2025-06-26 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(db_index=True, max_length=100)),
                ('download_link', models.URLField(db_index=True, unique=True)),
                ('used', models.BooleanField(db_index=True, default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'indexes': [models.Index(fields=['used', 'app_name'], name='deploy_appl_used_966210_idx')],
            },
        ),
    ]

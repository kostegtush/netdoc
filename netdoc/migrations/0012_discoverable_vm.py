# Generated by Django 4.1.8 on 2023-08-08 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtualization', '0034_standardize_description_comments'),
        ('netdoc', '0011_alter_credential_enable_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='discoverable',
            name='vm',
            field=models.OneToOneField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='virtualization.virtualmachine'),
        ),
    ]

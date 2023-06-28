# Generated by Django 4.1.6 on 2023-02-14 12:16

from django.db import migrations, models
import taggit.managers
import utilities.json


class Migration(migrations.Migration):
    dependencies = [
        (
            "netdoc",
            "0003_alter_arptableentry_options_alter_credential_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="macaddresstableentry",
            options={
                "ordering": ["mac_address", "vvid"],
                "verbose_name": "MAC Address table entry",
                "verbose_name_plural": "MAC Address table entries",
            },
        ),
        migrations.AlterModelOptions(
            name="routetableentry",
            options={
                "ordering": ["device", "protocol", "metric"],
                "verbose_name": "Route",
                "verbose_name_plural": "Routes",
            },
        ),
        migrations.CreateModel(
            name="Diagram",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "custom_field_data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder,
                    ),
                ),
                ("details", models.JSONField(default=dict, editable=False)),
                ("mode", models.CharField(max_length=30)),
                ("name", models.CharField(max_length=100)),
                (
                    "device_roles",
                    models.ManyToManyField(
                        blank=True, related_name="+", to="dcim.devicerole"
                    ),
                ),
                (
                    "sites",
                    models.ManyToManyField(
                        blank=True, related_name="+", to="dcim.site"
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        through="extras.TaggedItem", to="extras.Tag"
                    ),
                ),
                (
                    "vrfs",
                    models.ManyToManyField(blank=True, related_name="+", to="ipam.vrf"),
                ),
            ],
            options={
                "verbose_name": "Diagram",
                "verbose_name_plural": "Diagrams",
                "ordering": ["name"],
                "unique_together": {("name",)},
            },
        ),
    ]

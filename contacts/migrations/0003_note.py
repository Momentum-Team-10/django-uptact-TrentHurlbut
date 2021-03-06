# Generated by Django 3.2.9 on 2021-11-03 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0002_auto_20211103_1422"),
    ]

    operations = [
        migrations.CreateModel(
            name="Note",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(max_length=255)),
                ("published_date", models.DateTimeField(blank=True, null=True)),
                (
                    "about_contact",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contacts.contact",
                    ),
                ),
            ],
        ),
    ]

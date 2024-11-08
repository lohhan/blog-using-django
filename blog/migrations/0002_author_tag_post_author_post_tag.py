# Generated by Django 5.1.1 on 2024-11-05 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("first_name", models.CharField(max_length=80)),
                ("last_name", models.CharField(max_length=80)),
                ("email_adress", models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("caption", models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="blog.author"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(null=True, to="blog.tag"),
        ),
    ]

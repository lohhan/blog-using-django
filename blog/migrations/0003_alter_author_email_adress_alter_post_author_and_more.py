# Generated by Django 5.1.1 on 2024-11-05 23:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_author_tag_post_author_post_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="email_adress",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="posts",
                to="blog.author",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(
                validators=[django.core.validators.MinLengthValidator(10)]
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="excerpt",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="post",
            name="image_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(to="blog.tag"),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="tag",
            name="caption",
            field=models.CharField(max_length=20),
        ),
    ]

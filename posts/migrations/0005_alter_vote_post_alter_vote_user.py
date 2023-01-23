# Generated by Django 4.1.5 on 2023-01-16 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0004_alter_comment_post_alter_comment_reply_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vote",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pvotes",
                to="posts.post",
            ),
        ),
        migrations.AlterField(
            model_name="vote",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="uvotes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

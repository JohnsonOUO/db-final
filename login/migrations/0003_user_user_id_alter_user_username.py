# Generated by Django 4.1 on 2023-06-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0002_remove_user_id_alter_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_id",
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

# Generated by Django 5.1 on 2024-09-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_created_date_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]

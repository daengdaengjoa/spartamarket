# Generated by Django 4.2 on 2024-04-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_delete_likeditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='liked_items',
            field=models.ManyToManyField(related_name='liked_by_users', to='articles.item'),
        ),
    ]
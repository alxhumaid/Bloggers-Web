# Generated by Django 4.2.4 on 2023-08-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_alter_post_body_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('world', 'World'), ('politics', 'Politics'), ('india', 'India'), ('technology', 'Technology'), ('business', 'Business'), ('science', 'Science'), ('travel', 'Travel')], default='None', max_length=10),
        ),
    ]
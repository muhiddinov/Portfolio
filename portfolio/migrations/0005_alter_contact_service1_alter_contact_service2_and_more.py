# Generated by Django 5.0.6 on 2024-06-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_contact_service1_alter_contact_service2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='service1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='service2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='service3',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='service4',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='service5',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

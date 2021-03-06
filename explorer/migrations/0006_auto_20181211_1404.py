# Generated by Django 2.1.3 on 2018-12-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0005_auto_20181204_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='chainwork',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='hash',
            field=models.CharField(db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='block',
            name='height',
            field=models.IntegerField(db_index=True, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='input',
            unique_together={('block', 'commitment')},
        ),
        migrations.AlterUniqueTogether(
            name='output',
            unique_together={('block', 'commitment')},
        ),
    ]

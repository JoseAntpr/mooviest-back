# Generated by Django 2.0 on 2017-12-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='death',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'Female'), (2, 'Male')], null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='homepage',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='langs',
            field=models.ManyToManyField(blank=True, null=True, through='person.Person_lang', to='common.Lang'),
        ),
        migrations.AlterField(
            model_name='person',
            name='place_of_birthday',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

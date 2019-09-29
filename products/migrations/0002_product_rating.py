# Generated by Django 2.2.5 on 2019-09-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.CharField(choices=[('b', 'Bad'), ('a', 'Average'), ('e', 'Excellent')], default='a', max_length=1),
            preserve_default=False,
        ),
    ]

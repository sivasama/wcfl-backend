# Generated by Django 2.0.6 on 2018-06-04 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180604_0337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fixture',
            options={'ordering': ['id'], 'verbose_name_plural': 'Fixtures'},
        ),
        migrations.AlterModelOptions(
            name='squadlimit',
            options={'ordering': ['round'], 'verbose_name_plural': 'SquadLimits'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['id'], 'verbose_name_plural': 'Teams'},
        ),
    ]

# Generated by Django 4.1.5 on 2023-05-27 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_holiday_date_alter_holiday_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timeslot',
            options={'verbose_name': 'слот', 'verbose_name_plural': 'слоты'},
        ),
        migrations.AlterModelOptions(
            name='timeslottag',
            options={'verbose_name': 'тег', 'verbose_name_plural': 'теги'},
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='tags',
            field=models.ManyToManyField(blank=True, to='web.timeslottag', verbose_name='Теги'),
        ),
    ]

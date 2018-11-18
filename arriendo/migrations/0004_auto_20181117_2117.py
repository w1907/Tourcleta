# Generated by Django 2.1.2 on 2018-11-17 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arriendo', '0003_auto_20181117_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendo',
            name='a_bicicleta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Bicicleta'),
        ),
        migrations.AlterField(
            model_name='arriendo',
            name='a_equipamiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Equipamiento'),
        ),
    ]
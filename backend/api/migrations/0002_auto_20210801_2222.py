# Generated by Django 3.2.5 on 2021-08-01 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255, verbose_name='Логин')),
                ('money_spent', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='buyer',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='Stone',
        ),
        migrations.AddField(
            model_name='customer',
            name='stone',
            field=models.ManyToManyField(to='api.Product'),
        ),
        migrations.AlterField(
            model_name='purchasehistory',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer'),
        ),
        migrations.AlterField(
            model_name='purchasehistory',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product'),
        ),
    ]
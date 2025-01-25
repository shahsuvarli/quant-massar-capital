# Generated by Django 5.1.5 on 2025-01-25 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hedgefunds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric_name', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=4, max_digits=20)),
                ('as_of_date', models.DateField()),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_metrics', to='hedgefunds.portfolio')),
            ],
        ),
    ]

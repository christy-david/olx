# Generated by Django 4.2.7 on 2024-01-03 01:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_alter_transaction_credits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('coupon_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('coupon_code', models.CharField(max_length=255)),
                ('discount_value', models.IntegerField()),
                ('discount_type', models.CharField(choices=[('percentage', 'Percentage discount'), ('flat', 'Flat discount')], max_length=100)),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(default=169.0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='credits',
            field=models.IntegerField(default=1),
        ),
    ]

# Generated by Django 4.2.9 on 2024-02-03 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LittlelemonAPI', '0003_rename_order_orderitem_user_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderitem',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='LittlelemonAPI.order'),
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
    ]
# Generated by Django 4.1.1 on 2022-12-02 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('didii', '0005_remove_post_id_cmt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='duong',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='phuong_xa',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='quan_huyen',
            new_name='street',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='tinh_tp',
            new_name='ward',
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 4.1.1 on 2022-12-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('didii', '0003_remove_interact_id_remove_post_id_interact_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='id_cmt',
        ),
        migrations.AddField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, default=21, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='id_cmt',
            field=models.CharField(max_length=10),
        ),
    ]

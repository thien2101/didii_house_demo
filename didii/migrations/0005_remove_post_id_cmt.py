# Generated by Django 4.1.1 on 2022-12-02 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('didii', '0004_remove_comment_id_cmt_comment_id_alter_post_id_cmt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id_cmt',
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-19 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_reply_replyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='origin',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='posts.post'),
        ),
        migrations.AddField(
            model_name='post',
            name='repost',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='posts.post'),
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]

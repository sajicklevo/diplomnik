# Generated by Django 4.2.13 on 2024-08-27 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_friendshipstatus_delete_chat_alter_friendship_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_members', to='main.group')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_message', to='main.profile')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-27 18:30

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import tgbot.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50, unique=True)),
                ('registration_datetime', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(validators=[tgbot.models.validate_date_of_birth])),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[tgbot.models.validate_phone_number])),
                ('telegram_nickname', models.CharField(max_length=100, unique=True)),
                ('telegram_id', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_id', models.PositiveIntegerField()),
                ('tour_question_number_id', models.PositiveIntegerField()),
                ('question_text', models.TextField()),
                ('answer_a', models.CharField(max_length=250)),
                ('answer_b', models.CharField(max_length=250)),
                ('answer_c', models.CharField(max_length=250)),
                ('answer_d', models.CharField(max_length=250)),
                ('correct_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('explanation', models.TextField(max_length=1500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PointsTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_datetime', models.DateTimeField(auto_now_add=True)),
                ('tournament_points', models.PositiveIntegerField(null=True)),
                ('points_received_or_transferred', models.PositiveIntegerField(null=True)),
                ('bonuses', models.PositiveIntegerField(null=True)),
                ('transfer_datetime', models.DateTimeField(null=True)),
                ('points_transferred', models.PositiveIntegerField(null=True)),
                ('is_answered', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=False)),
                ('is_done', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=False)),
                ('receiver_telegram', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_transactions', to='tgbot.authorization', to_field='telegram_id')),
                ('sender_telegram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_transactions', to='tgbot.authorization', to_field='telegram_id')),
                ('transferor_telegram', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transferor_transactions', to='tgbot.authorization', to_field='telegram_id')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='tgbot.question')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_authorized', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_set', to='auth.permission')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.authorization')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.role')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='authorization',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbot.role'),
        ),
    ]

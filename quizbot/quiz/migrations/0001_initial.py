# Generated by Django 3.2.8 on 2021-10-27 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('points', models.PositiveIntegerField(verbose_name='points')),
                ('difficulty', models.IntegerField(choices=[(0, 'Any'), (1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert')], default=0, verbose_name='Difficulty')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Correct Answer')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='quiz.question', verbose_name='Question')),
            ],
        ),
    ]

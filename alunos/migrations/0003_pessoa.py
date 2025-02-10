# Generated by Django 4.2.18 on 2025-02-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0002_cidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
            ],
        ),
    ]

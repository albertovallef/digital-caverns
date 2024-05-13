# Generated by Django 4.2.11 on 2024-05-13 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, default='', max_length=30)),
                ('last_name', models.CharField(blank=True, default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_date', models.DateField(auto_now_add=True)),
                ('content', models.TextField(blank=True, default='', max_length=280)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('OK', 'Ok'), ('IGN', 'Ignore')], default='NEW', max_length=5)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_event', to='mysite.contact')),
            ],
        ),
    ]
# Generated by Django 2.2.10 on 2020-10-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Раздел статьи',
                'verbose_name_plural': 'Разделы статей',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='scope',
            field=models.ManyToManyField(to='articles.Scope'),
        ),
    ]

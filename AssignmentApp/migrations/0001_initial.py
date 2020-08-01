# Generated by Django 3.0.8 on 2020-07-31 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Provide course title.', max_length=30)),
                ('description', models.TextField(help_text='Provide course description.')),
                ('videofile', models.FileField(help_text='upload course vedio.', null=True, upload_to='deploy/videos/%Y/%m/%d/')),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
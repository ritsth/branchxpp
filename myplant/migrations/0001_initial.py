# Generated by Django 3.2.3 on 2021-10-18 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('type_text', models.CharField(max_length=200)),
                ('plant_img', models.ImageField(default='plant_img', upload_to='')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date published')),
                ('device', models.CharField(default='no devices in range', max_length=200)),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_name2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date published')),
                ('added_by', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_name4', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_photo', models.ImageField(default='d', upload_to='')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_name5', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default=' ', max_length=1200)),
                ('post_img', models.ImageField(default='post_img', upload_to='')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date published')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_name', to='myplant.addplant')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_name3', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=1200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date published')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_post', to='myplant.posts')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_name1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='myplant.question')),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-16 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_chapter_date_added_comic_image_page_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='chapter_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

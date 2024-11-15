# Generated by Django 5.1 on 2024-08-25 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="noticedb",
            fields=[
                ("noticeId", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=1000)),
                ("contents", models.TextField()),
                ("writeDate", models.DateTimeField(auto_now_add=True)),
                ("publishDate", models.DateTimeField()),
                ("expiryDate", models.DateTimeField()),
                ("publishType", models.CharField(max_length=1)),
                ("pushType", models.CharField(max_length=1)),
            ],
        ),
    ]

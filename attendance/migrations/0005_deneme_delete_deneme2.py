# Generated by Django 4.0.7 on 2022-08-31 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_deneme2_delete_deneme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deneme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(db_collation='Turkish_CI_AS', db_column='LastName', max_length=255)),
                ('imageFieldImg', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Deneme2',
                'verbose_name_plural': 'Deneme2',
                'db_table': 'Deneme',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Deneme2',
        ),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0002_movie_footage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('birth_year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('main_picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='main_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
# Generated by Django 3.0.1 on 2019-12-30 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20191230_0900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='author',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='content',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='star',
            new_name='Star',
        ),
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.AddField(
            model_name='review',
            name='Movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Reviews', to='api.Movie'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Movies', models.ManyToManyField(to='api.Movie')),
            ],
        ),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('imported_t', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DRAFT', 'DRAFT'), ('TRASH', 'TRASH'), ('PUBLISHED', 'PUBLISHED')], default='DRAFT', max_length=50, verbose_name='Status')),
                ('age', models.PositiveBigIntegerField(default=18, verbose_name='Age')),
            ],
        ),
    ]

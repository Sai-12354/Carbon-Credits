from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employerprofile',
            name='initial_credits_allocated',
            field=models.BooleanField(default=False),
        ),
    ] 
 
 
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),  # Make sure this points to the last applied migration
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='order',
            field=models.IntegerField(default=0),  # Use the default you want
        ),
    ]

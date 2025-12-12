# products/migrations/0002_rename_model.py
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',   # nombre antiguo tal como aparece en 0001_initial.py
            new_name='Product',    # nuevo nombre de la clase en models.py
        ),
    ]

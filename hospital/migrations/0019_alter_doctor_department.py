from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('General Physician', 'General Physician'), ('Paediatrician', 'Paediatrician'), ('Neurologist', 'Neurologist'), ('Cardiologist', 'Cardiologist'), ('Dentist', 'Dentist'), ('Ophthalmologist', 'Ophthalmologist'), ('Dermatologist', 'Dermatologist'), ('Orthopedic doctor', 'Orthopedic doctor'), ('Gynecologist', 'Gynecologist'), ('Surgeon', 'Surgeon')], default='General Physician', max_length=50),
        ),
    ]

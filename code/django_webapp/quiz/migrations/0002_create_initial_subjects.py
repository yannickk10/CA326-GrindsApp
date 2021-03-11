from django.db import migrations


def create_subjects(apps, schema_editor):
    Subject = apps.get_model('quiz', 'Subject')
    Subject.objects.create(name='Arts', color='#f44336')
    Subject.objects.create(name='Computing', color='#007bff')
    Subject.objects.create(name='Math', color='#651fff')
    Subject.objects.create(name='Biology', color='#17a2b8')
    Subject.objects.create(name='History', color='#ffc107')
    Subject.objects.create(name='English', color='#e65100')
    Subject.objects.create(name='Geography', color='#28a745')




class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects),
    ]

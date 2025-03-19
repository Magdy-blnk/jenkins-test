from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

    def add_example_data(apps, schema_editor):
        ExampleModel = apps.get_model('your_app_name', 'ExampleModel')
        ExampleModel.objects.create(name='Example Data')

    operations.append(
        migrations.RunPython(add_example_data)
    )
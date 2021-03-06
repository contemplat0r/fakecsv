# Generated by Django 3.1.7 on 2021-03-01 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(max_length=256, verbose_name='schema name')),
            ],
        ),
        migrations.CreateModel(
            name='SchemaColumnType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_column_type_name', models.CharField(max_length=64, unique=True, verbose_name='schema column type name')),
            ],
        ),
        migrations.CreateModel(
            name='SchemaColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=128, verbose_name='schema column name')),
                ('column_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataschemas.schemacolumntype', verbose_name='schema column type')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataschemas.schema', verbose_name='schema column type')),
            ],
        ),
        migrations.AddField(
            model_name='schema',
            name='schema_column',
            field=models.ManyToManyField(through='dataschemas.SchemaColumn', to='dataschemas.SchemaColumnType', verbose_name='column'),
        ),
    ]

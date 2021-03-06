# Generated by Django 3.0.3 on 2020-02-12 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hf_1',
            field=models.CharField(blank=True, choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('SF', 'Satisfactory'), ('NI', 'Needs Improvement')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='hf_3',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='hf_4',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='hf_5',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='hf_6',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='hf_7',
            field=models.CharField(blank=True, choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('SF', 'Satisfactory'), ('NI', 'Needs Improvement')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='sch_2',
            field=models.CharField(blank=True, choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('SF', 'Satisfactory'), ('NI', 'Needs Improvement')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='sch_3',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='sch_4',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='sch_4b',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='sch_5',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='sch_6',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='st_1',
            field=models.CharField(blank=True, choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('SF', 'Satisfactory'), ('NI', 'Needs Improvement')], max_length=3),
        ),
        migrations.AlterField(
            model_name='post',
            name='st_4',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='st_5',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='st_6',
            field=models.CharField(blank=True, choices=[('EX', 'Excellent'), ('VG', 'Very Good'), ('SF', 'Satisfactory'), ('NI', 'Needs Improvement')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='st_7',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='st_7a',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10),
        ),
    ]

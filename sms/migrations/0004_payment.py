# Generated by Django 4.1.6 on 2023-02-21 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_student_rf_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, null=True)),
                ('month', models.CharField(choices=[('jan', 'jan'), ('feb', 'feb'), ('mar', 'mar'), ('apr', 'apr'), ('may', 'may'), ('jun', 'jun'), ('jul', 'jul'), ('aug', 'aug'), ('sept', 'sept'), ('oct', 'oct'), ('nov', 'nov'), ('dec', 'dec')], max_length=10)),
                ('is_paid', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='sms.student')),
            ],
        ),
    ]
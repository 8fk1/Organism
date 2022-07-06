# Generated by Django 4.0.5 on 2022-07-05 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organism', '0005_alter_organism_domain_alter_organism_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organism',
            name='family',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organism', to='organism.family', verbose_name='科'),
        ),
        migrations.AlterField(
            model_name='organism',
            name='kingdom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organism', to='organism.kingdom', verbose_name='界'),
        ),
    ]

# Generated by Django 2.2.2 on 2019-08-04 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("xr_newsletter", "0014_add_field_name_to_emailformfield")]

    operations = [
        migrations.AddField(
            model_name="emailformfield",
            name="size",
            field=models.CharField(
                choices=[("1_3", "1/3"), ("1_2", "1/2"), ("2_3", "2/3"), ("1_1", "1")],
                default="1_3",
                help_text="The width of the field.",
                max_length=255,
                verbose_name="Size",
            ),
        ),
        migrations.AddField(
            model_name="newsletterformfield",
            name="size",
            field=models.CharField(
                choices=[("1_3", "1/3"), ("1_2", "1/2"), ("2_3", "2/3"), ("1_1", "1")],
                default="1_3",
                help_text="The width of the field.",
                max_length=255,
                verbose_name="Size",
            ),
        ),
        migrations.AlterField(
            model_name="emailformfield",
            name="placeholder",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Wird in grau angezeigt und verschwindet sobald das Feld fokusiert wird.",
                max_length=255,
                verbose_name="Platzhalter",
            ),
        ),
        migrations.AlterField(
            model_name="newsletterformfield",
            name="placeholder",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Wird in grau angezeigt und verschwindet sobald das Feld fokusiert wird.",
                max_length=255,
                verbose_name="Platzhalter",
            ),
        ),
    ]

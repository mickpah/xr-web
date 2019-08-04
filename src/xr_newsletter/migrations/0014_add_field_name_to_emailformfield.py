# Generated by Django 2.2.2 on 2019-08-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("xr_newsletter", "0013_remove_field_thank_you_text")]

    operations = [
        migrations.AlterModelOptions(
            name="thankyoupage",
            options={
                "verbose_name": "Danke Seite",
                "verbose_name_plural": "Danke Seiten",
            },
        ),
        migrations.AddField(
            model_name="emailformfield",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Ein eindeutiger Name für das Formularfeld",
                max_length=255,
                null=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="newsletterformfield",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Ein eindeutiger Name für das Formularfeld",
                max_length=255,
                null=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="emailformfield", unique_together={("page", "name")}
        ),
    ]

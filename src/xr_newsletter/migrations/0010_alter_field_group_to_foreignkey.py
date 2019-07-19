# Generated by Django 2.2.2 on 2019-07-19 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("xr_newsletter", "0009_add_fields_placholder_and_mautic_form_id")]

    operations = [
        migrations.AlterField(
            model_name="newsletterformpage",
            name="group",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.PROTECT,
                to="xr_pages.LocalGroup",
            ),
        )
    ]

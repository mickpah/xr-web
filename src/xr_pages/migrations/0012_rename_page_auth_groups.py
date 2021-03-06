# Generated by Django 2.1.7 on 2019-03-17 19:31

from django.db import migrations


def rename_page_auth_groups(apps, schema_editor):
    Group = apps.get_model("auth.Group")

    # rename existing page auth groups
    for group_type in ["Editors", "Moderators"]:
        group_qs = Group.objects.filter(name__endswith=group_type)

        for group in group_qs:
            if group.name == "Overall Site %s" % group_type:
                # exclude Overall Site Editors and Moderators groups
                continue
            group_name = group.name[: -len(group_type)]
            group_name += "Page %s" % group_type
            group.name = group_name
            group.save()


class Migration(migrations.Migration):

    dependencies = [("xr_pages", "0011_adjust_localgrouplistpage_pagerevisions")]

    operations = [
        migrations.RunPython(rename_page_auth_groups, migrations.RunPython.noop)
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-21 09:57


from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("orgs", "0023_orgbackend")]

    def populate_org_backend(apps, schema_editor):
        Org = apps.get_model("orgs", "Org")
        OrgBackend = apps.get_model("orgs", "OrgBackend")
        orgs = Org.objects.all()
        User = apps.get_model("auth", "User")
        root = User.objects.filter(username="root").first()

        if not root:
            root = User.objects.filter(username="root2").first()

        if not root:
            root = User.objects.create(username="root2")

        default_backend = getattr(settings, "SITE_BACKEND", None)
        host = getattr(settings, "SITE_API_HOST", None)

        for org in orgs:
            if not org.config:
                continue

            config = org.config
            rapidpro_config = config.get("rapidpro", dict())
            api_token = rapidpro_config.get("api_token", "")
            OrgBackend.objects.create(
                org=org,
                slug="rapidpro",
                api_token=api_token,
                host=host,
                backend_type=default_backend,
                created_by=root,
                modified_by=root,
            )

            del rapidpro_config["api_token"]
            config["rapipro"] = rapidpro_config
            org.config = config
            org.save()

    def noop(apps, schema_editor):
        pass

    operations = [migrations.RunPython(populate_org_backend, noop)]

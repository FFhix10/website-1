# Generated by Django 2.0.7 on 2018-11-13 23:39

import vies.models
from django.db import migrations

import wlhosted.payments.validators


class Migration(migrations.Migration):

    dependencies = [("payments", "0008_auto_20181106_1622")]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="vat",
            field=vies.models.VATINField(
                blank=True,
                help_text=(
                    "Please fill in European Union VAT ID, "
                    "leave blank if not applicable."
                ),
                max_length=14,
                null=True,
                validators=[wlhosted.payments.validators.validate_vatin],
                verbose_name="European VAT ID",
            ),
        )
    ]

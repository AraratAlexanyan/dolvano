# Generated by Django 4.1.5 on 2023-03-01 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Ժամացույց")),
                ("product_code", models.CharField(max_length=200, verbose_name="Կոդ")),
                ("mini_description", models.TextField(verbose_name="Փոքր նկարագիր")),
                (
                    "card_photo",
                    models.ImageField(
                        upload_to="clock_photos/", verbose_name="Քարտի նկար 220x220"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Գինը"
                    ),
                ),
                (
                    "background_photo",
                    models.ImageField(
                        upload_to="clock_photos/", verbose_name="Բաների նկար"
                    ),
                ),
                (
                    "info_image_1",
                    models.ImageField(upload_to="clock_photos/", verbose_name="Ինֆո 1"),
                ),
                ("info_description_1", models.TextField(verbose_name="Ինֆո 1 նկար")),
                (
                    "info_image_2",
                    models.ImageField(upload_to="clock_photos/", verbose_name="Ինֆո 2"),
                ),
                ("info_description_2", models.TextField(verbose_name="Ինֆո 2 նկար")),
                (
                    "info_image_3",
                    models.ImageField(upload_to="clock_photos/", verbose_name="Ինֆո 3"),
                ),
                ("info_description_3", models.TextField(verbose_name="Ինֆո 3 նկար")),
                (
                    "slider_photo_1",
                    models.ImageField(
                        upload_to="clock_photos/", verbose_name="սլայդի նկար 1"
                    ),
                ),
                (
                    "slider_photo_2",
                    models.ImageField(
                        upload_to="clock_photos/", verbose_name="սլայդի նկար 2"
                    ),
                ),
                (
                    "slider_photo_3",
                    models.ImageField(
                        upload_to="clock_photos/", verbose_name="սլայդի նկար 3"
                    ),
                ),
                (
                    "slider_photo_4",
                    models.ImageField(
                        upload_to="clock_photos/", verbose_name="սլայդի նկար 4"
                    ),
                ),
                (
                    "slider_photo_5",
                    models.ImageField(
                        upload_to="clock_photos/", verbose_name="սլայդի նկար 5"
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(auto_now_add=True, verbose_name="Ամսաթիվ"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Information",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image1", models.ImageField(upload_to="info/")),
                ("description1", models.TextField()),
                ("image2", models.ImageField(upload_to="info/")),
                ("description2", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Rubric",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=20, verbose_name="Անվանում"
                    ),
                ),
            ],
            options={
                "verbose_name": "Ռուբրիկա",
                "verbose_name_plural": "Ռուբրիկաներ",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="WallClock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image1", models.ImageField(upload_to="wallclocks/")),
                ("image2", models.ImageField(upload_to="wallclocks/")),
                ("image3", models.ImageField(upload_to="wallclocks/")),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "published",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Հրատարակված է"
                    ),
                ),
                (
                    "rubric",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="main.rubric",
                        verbose_name="Ռուբրիկա",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Decoration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image1", models.ImageField(upload_to="wallclocks/")),
                ("image2", models.ImageField(upload_to="wallclocks/")),
                ("image3", models.ImageField(upload_to="wallclocks/")),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "published",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Հրատարակված է"
                    ),
                ),
                (
                    "rubric",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="main.rubric",
                        verbose_name="Ռուբրիկա",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-09 07:42

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.SlugField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(db_index=True, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=255)),
                ('mrp', models.FloatField(verbose_name='M.R.P.')),
                ('discount', models.IntegerField(verbose_name='Discount %')),
                ('price', models.FloatField()),
                ('brand', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('supported_devices', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('origin', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('imageurl', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='materials',
            field=models.ManyToManyField(to='products.ProductMaterial'),
        ),
    ]

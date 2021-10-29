from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=models.deletion.CASCADE, to='order.product')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user',
                 models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='followers',
                                   to='order.user')),
                ('to_user', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='following',
                                              to='order.user')),
            ],
        ),
    ]

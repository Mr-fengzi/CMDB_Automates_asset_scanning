# Generated by Django 2.2 on 2020-07-10 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_asset_type', models.SmallIntegerField(choices=[(0, 'PC服务器'), (1, '刀片机'), (2, '小型机')], default=0, verbose_name='服务器类型')),
                ('created_by', models.CharField(choices=[('auto', '自动添加'), ('manual', '手工录入')], default='auto', max_length=32, verbose_name='添加方式')),
                ('IP', models.CharField(default='', max_length=30, verbose_name='IP地址')),
                ('MAC', models.CharField(default='', max_length=200, verbose_name='Mac地址')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='服务器型号')),
                ('hostname', models.CharField(blank=True, max_length=128, null=True, verbose_name='主机名')),
                ('os_type', models.CharField(blank=True, max_length=64, null=True, verbose_name='操作系统类型')),
                ('os_distribution', models.CharField(blank=True, max_length=64, null=True, verbose_name='发行商')),
                ('os_release', models.CharField(blank=True, max_length=64, null=True, verbose_name='操作系统版本')),
                ('hosted_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosted_on_server', to='scanhost.Server', verbose_name='宿主机')),
            ],
            options={
                'verbose_name': '服务器',
                'verbose_name_plural': '服务器',
            },
        ),
    ]
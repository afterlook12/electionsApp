# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 11:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electionscandidates',
            old_name='candidates_id',
            new_name='candidates',
        ),
        migrations.RenameField(
            model_name='electionscandidates',
            old_name='elections_id',
            new_name='elections',
        ),
        migrations.RenameField(
            model_name='electionspriviliged',
            old_name='elections_id',
            new_name='elections',
        ),
        migrations.RenameField(
            model_name='electionspriviliged',
            old_name='electors_id',
            new_name='electors',
        ),
    ]

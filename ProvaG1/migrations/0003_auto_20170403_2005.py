# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProvaG1', '0002_evento_id_eventocientifico'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipoInscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_Inscricao', models.CharField(max_length=200, verbose_name='tipo_inscricao')),
            ],
        ),
        migrations.RemoveField(
            model_name='artigocientifico',
            name='id_evento',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='id_artigo',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='id_eventoCientifico',
        ),
        migrations.RemoveField(
            model_name='participante',
            name='tipoInscricao',
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='autores',
            field=models.ManyToManyField(to='ProvaG1.Autor'),
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ProvaG1.Evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='id_pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProvaG1.Pessoa'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='id_evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProvaG1.Evento'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='id_pessoaFisica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProvaG1.PessoaFisica'),
        ),
        migrations.AddField(
            model_name='participante',
            name='id_tipoInscricao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ProvaG1.tipoInscricao'),
        ),
    ]

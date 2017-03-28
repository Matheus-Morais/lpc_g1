from django.db import models
from django.utils import timezone

class Evento(models.Model):
    nome = models.CharField('nome', max_length=200)
    eventoPrincipal = models.CharField('evento_principal', max_length=200)
    sigla = models.CharField('sigla', max_length=200)
    dataEHoradeInicio = models.DateTimeField('dataeHora_inicio', default=timezone.now)
    palavraChave = models.CharField('palavra_chave', max_length=200)
    logotipo = models.CharField('logotipo', max_length=200)
    id_pessoa = models.IntegerField('id_pessoa', null = False)
    cidade = models.CharField('cidade', max_length=200)
    uf = models.CharField('uf', max_length=200)
    endereco = models.CharField('endereco', max_length=200)
    cep = models.CharField('cep', max_length=200)
    id_eventoCientifico = models.IntegerField('id_eventoCientifico', null = True)

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.CharField('email', max_length=200)

class Autor(Pessoa):
    curriculo = models.CharField('curriculo', max_length=200)
    id_artigo = models.IntegerField('id_artigo', null = True)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField('cnpj', max_length=200)
    razaoSocial = models.CharField('razaoSocial', max_length=200)

class PessoaFisica(Pessoa):
    cpf = models.CharField('cpf', max_length=11)

class Participante(models.Model):
    dataEHoradeInscricao = models.DateTimeField('dataeHora_inscricao', default=timezone.now)
    tipoInscricao = models.CharField('tipo_inscricao', max_length=200)
    id_pessoaFisica = models.IntegerField('id_pessoaFisica', null = False)
    id_evento = models.IntegerField('id_evento', null = False)

class EventoCientifico(Evento):
    issn = models.CharField('issn', max_length=200)

class ArtigoCientifico(models.Model):
    titulo = models.CharField('titulo', max_length=200)
    id_evento = models.IntegerField('id_evento', null = True)

from django.db import models
from django.utils import timezone

class Evento(models.Model):
    nome = models.CharField('nome', max_length=200)
    eventoPrincipal = models.CharField('evento_principal', max_length=200)
    sigla = models.CharField('sigla', max_length=200)
    dataEHoradeInicio = models.DateTimeField('dataeHora_inicio', default=timezone.now)
    palavraChave = models.CharField('palavra_chave', max_length=200)
    logotipo = models.CharField('logotipo', max_length=200)
    id_pessoa = models.ForeignKey('Pessoa')
    cidade = models.CharField('cidade', max_length=200)
    uf = models.CharField('uf', max_length=200)
    endereco = models.CharField('endereco', max_length=200)
    cep = models.CharField('cep', max_length=200)

class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=200)
    email = models.CharField('email', max_length=200)

class Autor(Pessoa):
    curriculo = models.CharField('curriculo', max_length=200)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField('cnpj', max_length=200)
    razaoSocial = models.CharField('razaoSocial', max_length=200)

class PessoaFisica(Pessoa):
    cpf = models.CharField('cpf', max_length=11)

class Participante(models.Model):
    dataEHoradeInscricao = models.DateTimeField('dataeHora_inscricao', default=timezone.now)
    id_pessoaFisica = models.ForeignKey('PessoaFisica')
    id_evento = models.ForeignKey('Evento')
    id_tipoInscricao = models.ForeignKey('tipoInscricao', null = True)

class tipoInscricao(models.Model):
    tipo_Inscricao = models.CharField('tipo_inscricao', max_length=200)

class EventoCientifico(Evento):
    issn = models.CharField('issn', max_length=200)

class ArtigoCientifico(models.Model):
    titulo = models.CharField('titulo', max_length=200)
    evento = models.ForeignKey('Evento', null = True)
    autores = models.ManyToManyField(Autor)

from django.shortcuts import render
from django.http import HttpResponse

from .models import Evento
from .models import Pessoa
from .models import EventoCientifico
from .models import ArtigoCientifico
from .models import PessoaFisica
from .models import PessoaJuridica
from .models import Autor
from .models import Participante


def inscricoes(id_evento):
    part = Participante.objects.all()
    cont = 0
    for p in part:
        if(p.id_evento == id_evento):
            cont = cont + 1
    return str(cont)

def Eventos(request):
    html = "<h1>Lista de Eventos</h1>"
    lista = Evento.objects.all()
    eventoC = EventoCientifico.objects.all()
    pessoa = Pessoa.objects.all()
    for evento in lista:
        #autor = Pessoa.objects.filter(id = evento.id_pessoa)
        for autores in pessoa:
            if(evento.id_pessoa == autores.id):
                autor = autores.nome
        for cientifico in eventoC:
            if(evento.id == cientifico.id):
                eventoCientifico = cientifico.issn
            else:
                eventoCientifico = 'Não é evento cientifico'

        html += '<li>{}</li>'.format('<br/>Nome do Evento: ' + evento.nome + '<br/>Evento Principal: '+ evento.eventoPrincipal +
                                     '<br/>Sigla: '+ evento.sigla+ '<br/>Data e Hora de Inicio: '+ str(evento.dataEHoradeInicio) +
                                     '<br/>Palavra Chave: ' + evento.palavraChave+ '<br/>Logotipo: '+ evento.logotipo + '<br/>Autor: '
                                     +  autor +'<br/>Cidade: ' + evento.cidade +'-'+ evento.uf + '<br/>Endereço: '+
                                     evento.endereco+ '<br/>ISSN: '+ eventoCientifico + "<br/>Inscrições: " + inscricoes(evento.id))

    html += '<br/><h3>Para escolher um determinado evento, no navegador apague o "s/" de "eventos/"e acrescente na frente da url "/id"<h3>'
    return HttpResponse(html)

def EventoX(request, id):
    html = "<h1>Determinado Evento</h1>"
    evento = Evento.objects.get(pk=id)
    eventoC = EventoCientifico.objects.all()
    pessoa = Pessoa.objects.all()
    #for evento in lista:
        #if(evento.id == id):
    for autores in pessoa:
        if (evento.id_pessoa == autores.id):
            autor = autores.nome
    for cientifico in eventoC:
        if (evento.id == cientifico.id):
            eventoCientifico = cientifico.issn
        else:
            eventoCientifico = 'Não é evento cientifico'

    html += '<li>{}</li>'.format(
                '<br/>Nome do Evento: ' + evento.nome + '<br/>Evento Principal: ' + evento.eventoPrincipal +
                '<br/>Sigla: ' + evento.sigla + '<br/>Data e Hora de Inicio: ' + str(evento.dataEHoradeInicio) +
                '<br/>Palavra Chave: ' + evento.palavraChave + '<br/>Logotipo: ' + evento.logotipo + '<br/>Autor: '
                + autor + '<br/>Cidade: ' + evento.cidade + '-' + evento.uf + '<br/>Endereço: ' +
                evento.endereco + '<br/>ISSN: ' + eventoCientifico + "<br/>Inscrições: " + inscricoes(evento.id))

    return HttpResponse(html)

def Pessoas(request):
    html = "<h1>Lista de Pessoas</h1>"
    lista = Pessoa.objects.all()
    pf = PessoaFisica.objects.all()
    pj = PessoaJuridica.objects.all()
    for pessoa in lista:
        for pef in pf:
            if(pef.id == pessoa.id):
                tipo = 'Pessoa Fisica'
                html += '<li>{}</li>'.format('<br/>Nome: '+ pessoa.nome +'<br/>Email: '+ pessoa.email + '<br/>Tipo: '+ tipo + '<br/>CPF: '+pef.cpf)
        for pej in pj:
            if( pej.id == pessoa.id):
                tipo = 'Pessoa Juridica'
                html += '<li>{}</li>'.format('<br/>Nome: ' + pessoa.nome + '<br/>Email: ' + pessoa.email + '<br/>Tipo: ' + tipo + '<br/>CNPJ: ' + pej.cnpj)

    html += '<br/><h3>Para escolher uma determinada Pessoa, no navegador apague o "s/" de "Pessoas/"e acrescente na frente da url "/id"<h3>'
    return HttpResponse(html)

def PessoaX(request, id):
    html = "<h1>Determinada Pessoa</h1>"
    pessoa = Pessoa.objects.get(pk=id)
    pf = PessoaFisica.objects.all()
    pj = PessoaJuridica.objects.all()
    for pef in pf:
        if (pef.id == pessoa.id):
            tipo = 'Pessoa Fisica'
            html += '<li>{}</li>'.format(
                '<br/>Nome: ' + pessoa.nome + '<br/>Email: ' + pessoa.email + '<br/>Tipo: ' + tipo + '<br/>CPF: ' + pef.cpf)
    for pej in pj:
        if (pej.id == pessoa.id):
            tipo = 'Pessoa Juridica'
            html += '<li>{}</li>'.format(
                '<br/>Nome: ' + pessoa.nome + '<br/>Email: ' + pessoa.email + '<br/>Tipo: ' + tipo + '<br/>CNPJ: ' + pej.cnpj)
    return HttpResponse(html)

def Artigos(request):
    html = "<h1>Lista de Artigos</h1>"
    artigos = ArtigoCientifico.objects.all()
    autores = Autor.objects.all()
    for artigo in artigos:
        for autor in autores:
            if(artigo.id == autor.id_artigo):
                html += '<li>{}</li>'.format('<br/> Nome do Artigo: ' + artigo.titulo + "<br/> Autor: " + autor.nome + "<br/> Curriculo: "+ autor.curriculo)

    return HttpResponse(html)

def ArtigoX(request, id):
    html = "<h1>Lista de Artigos</h1>"
    artigo = ArtigoCientifico.objects.get(pk=id)
    autores = Autor.objects.all()
    for autor in autores:
        if (artigo.id == autor.id_artigo):
            html += '<li>{}</li>'.format(
                '<br/> Nome do Artigo: ' + artigo.titulo + "<br/> Autor: " + autor.nome + "<br/> Curriculo: " + autor.curriculo)

    return HttpResponse(html)

def Recursos(request):
    html = "<h1>Lista de Eventos</h1>"
    lista = Evento.objects.all()
    eventoC = EventoCientifico.objects.all()
    pessoa = Pessoa.objects.all()
    for evento in lista:
        # autor = Pessoa.objects.filter(id = evento.id_pessoa)
        for autores in pessoa:
            if (evento.id_pessoa == autores.id):
                autor = autores.nome
        for cientifico in eventoC:
            if (evento.id == cientifico.id):
                eventoCientifico = cientifico.issn
            else:
                eventoCientifico = 'Não é evento cientifico'

        html += '<li>{}</li>'.format(
            '<br/>Nome do Evento: ' + evento.nome + '<br/>Evento Principal: ' + evento.eventoPrincipal +
            '<br/>Sigla: ' + evento.sigla + '<br/>Data e Hora de Inicio: ' + str(evento.dataEHoradeInicio) +
            '<br/>Palavra Chave: ' + evento.palavraChave + '<br/>Logotipo: ' + evento.logotipo + '<br/>Autor: '
            + autor + '<br/>Cidade: ' + evento.cidade + '-' + evento.uf + '<br/>Endereço: ' +
            evento.endereco + '<br/>ISSN: ' + eventoCientifico + "<br/>Inscrições: " + inscricoes(evento.id))


    html += "<br/><br/><br/> <h1>Lista de Pessoas</h1>"
    lista = Pessoa.objects.all()
    pf = PessoaFisica.objects.all()
    pj = PessoaJuridica.objects.all()
    for pessoa in lista:
        for pef in pf:
            if (pef.id == pessoa.id):
                tipo = 'Pessoa Fisica'
                html += '<li>{}</li>'.format(
                    '<br/>Nome: ' + pessoa.nome + '<br/>Email: ' + pessoa.email + '<br/>Tipo: ' + tipo + '<br/>CPF: ' + pef.cpf)
        for pej in pj:
            if (pej.id == pessoa.id):
                tipo = 'Pessoa Juridica'
                html += '<li>{}</li>'.format(
                    '<br/>Nome: ' + pessoa.nome + '<br/>Email: ' + pessoa.email + '<br/>Tipo: ' + tipo + '<br/>CNPJ: ' + pej.cnpj)
    html += "<br/><br/><br/><h1>Lista de Artigos</h1>"
    artigos = ArtigoCientifico.objects.all()
    autores = Autor.objects.all()
    for artigo in artigos:
        for autor in autores:
            if (artigo.id == autor.id_artigo):
                html += '<li>{}</li>'.format(
                    '<br/> Nome do Artigo: ' + artigo.titulo + "<br/> Autor: " + autor.nome + "<br/> Curriculo: " + autor.curriculo)

    return HttpResponse(html)


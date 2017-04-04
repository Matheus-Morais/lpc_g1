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
    pessoas = PessoaFisica.objects.all()
    cont = ''
    for p in part:
        if(p.id_evento_id == id_evento):
            for nome in pessoas:
                if(nome.id == p.id_pessoaFisica.id):
                    cont += '<br/>'+ nome.nome
    return str(cont)

def Eventos(request):
    html = "<h1>Lista de Eventos</h1>"
    lista = Evento.objects.all()
    eventoC = EventoCientifico.objects.all()
    pessoa = Pessoa.objects.all()
    for evento in lista:
        for cientifico in eventoC:
            x = cientifico.id
            if(evento.id == x):
                eventoCientifico = cientifico.issn
            else:
                eventoCientifico = 'Não é evento cientifico'

        html += '<li>{}</li>'.format('<br/>Nome do Evento: ' + evento.nome + '<br/>Evento Principal: '+ evento.eventoPrincipal +
                                     '<br/>Sigla: '+ evento.sigla+ '<br/>Data e Hora de Inicio: '+ str(evento.dataEHoradeInicio) +
                                     '<br/>Palavra Chave: ' + evento.palavraChave+ '<br/>Logotipo: '+ evento.logotipo + '<br/>Autor: '
                                     +  evento.id_pessoa.nome +'<br/>Cidade: ' + evento.cidade +'-'+ evento.uf + '<br/>Endereço: '+
                                     evento.endereco+ '<br/>ISSN: '+ eventoCientifico + "<br/>Inscrições: " + inscricoes(evento.id))

    html += '<br/><h3>Para escolher um determinado evento, no navegador apague o "s/" de "eventos/"e acrescente na frente da url "/id"<h3>'
    return HttpResponse(html)

def EventoX(request, id):
    html = "<h1>Determinado Evento</h1>"
    evento = Evento.objects.get(pk=id)
    eventoC = EventoCientifico.objects.all()
    pessoa = Pessoa.objects.all()
    for cientifico in eventoC:
        x = cientifico.id
        if(evento.id == x):
            eventoCientifico = cientifico.issn
        else:
            eventoCientifico = 'Não é evento cientifico'

    html += '<li>{}</li>'.format('<br/>Nome do Evento: ' + evento.nome + '<br/>Evento Principal: '+ evento.eventoPrincipal +
                                     '<br/>Sigla: '+ evento.sigla+ '<br/>Data e Hora de Inicio: '+ str(evento.dataEHoradeInicio) +
                                     '<br/>Palavra Chave: ' + evento.palavraChave+ '<br/>Logotipo: '+ evento.logotipo + '<br/>Autor: '
                                     +  evento.id_pessoa.nome +'<br/>Cidade: ' + evento.cidade +'-'+ evento.uf + '<br/>Endereço: '+
                                     evento.endereco+ '<br/>ISSN: '+ eventoCientifico + "<br/>Inscrições: " + inscricoes(evento.id))

    return HttpResponse(html)

def Pessoas(request):
    html = "<h1>Lista de Pessoas</h1>"
    lista = Pessoa.objects.all()
    pf = PessoaFisica.objects.all()
    pj = PessoaJuridica.objects.all()
    au = Autor.objects.all()
    pa = Participante.objects.all()
    for pessoa in lista:
        for aut in au:
            if(aut.id == pessoa.id):
                tipo = 'Autor'
                html += '<li>{}</li>'.format('<br/>Nome: '+ pessoa.nome +'<br/>Email: '+ pessoa.email + '<br/>Tipo: '+ tipo + '<br/>CPF: '+aut.curriculo)


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
    au = Autor.objects.all()
    pj = PessoaJuridica.objects.all()
    for aut in au:
        if(aut.id == pessoa.id):
            tipo = 'Autor'
            html += '<li>{}</li>'.format('<br/>Nome: '+ pessoa.nome +'<br/>Email: '+ pessoa.email + '<br/>Tipo: '+ tipo + '<br/>CPF: '+aut.curriculo)

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
    x = 'Autores: '
    for artigo in artigos:
        for autor in artigo.autores.all():
                x += autor.nome + " | "
        html += '<li>{}</li>'.format('<br/> Nome do Artigo: ' + artigo.titulo + "<br/>"+x)

    return HttpResponse(html)

def ArtigoX(request, id):
    html = "<h1>Artigo</h1>"
    artigo = ArtigoCientifico.objects.get(pk=id)
    x = 'Autores: '
    for autor in artigo.autores.all():
            x += autor.nome + " | "
    html += '<li>{}</li>'.format('<br/> Nome do Artigo: ' + artigo.titulo + "<br/>"+x)

    return HttpResponse(html)

def Recursos(request):
    html = "<h1>Lista de Eventos</h1>"
    lista = Evento.objects.all()
    eventoC = EventoCientifico.objects.all()
    pessoa = Pessoa.objects.all()
    for evento in lista:
        for cientifico in eventoC:
            x = cientifico.id
            if(evento.id == x):
                eventoCientifico = cientifico.issn
            else:
                eventoCientifico = 'Não é evento cientifico'

        html += '<li>{}</li>'.format('<br/>Nome do Evento: ' + evento.nome + '<br/>Evento Principal: '+ evento.eventoPrincipal +
                                     '<br/>Sigla: '+ evento.sigla+ '<br/>Data e Hora de Inicio: '+ str(evento.dataEHoradeInicio) +
                                     '<br/>Palavra Chave: ' + evento.palavraChave+ '<br/>Logotipo: '+ evento.logotipo + '<br/>Autor: '
                                     +  evento.id_pessoa.nome +'<br/>Cidade: ' + evento.cidade +'-'+ evento.uf + '<br/>Endereço: '+
                                     evento.endereco+ '<br/>ISSN: '+ eventoCientifico + "<br/>Inscrições: " + inscricoes(evento.id))

    html += "<br/><br/><br/><h1>Lista de Pessoas</h1>"
    lista = Pessoa.objects.all()
    pf = PessoaFisica.objects.all()
    pj = PessoaJuridica.objects.all()
    au = Autor.objects.all()
    pa = Participante.objects.all()
    for pessoa in lista:
        for aut in au:
            if(aut.id == pessoa.id):
                tipo = 'Autor'
                html += '<li>{}</li>'.format('<br/>Nome: '+ pessoa.nome +'<br/>Email: '+ pessoa.email + '<br/>Tipo: '+ tipo + '<br/>CPF: '+aut.curriculo)


        for pef in pf:
            if(pef.id == pessoa.id):
                tipo = 'Pessoa Fisica'
                html += '<li>{}</li>'.format('<br/>Nome: '+ pessoa.nome +'<br/>Email: '+ pessoa.email + '<br/>Tipo: '+ tipo + '<br/>CPF: '+pef.cpf)

        for pej in pj:
            if( pej.id == pessoa.id):
                tipo = 'Pessoa Juridica'
                html += '<li>{}</li>'.format('<br/>Nome: ' + pessoa.nome + '<br/>Email: ' + pessoa.email + '<br/>Tipo: ' + tipo + '<br/>CNPJ: ' + pej.cnpj)

    html += "<br/><br/><br/><h1>Lista de Artigos</h1>"
    artigos = ArtigoCientifico.objects.all()
    x = 'Autores: '
    for artigo in artigos:
        for autor in artigo.autores.all():
                x += autor.nome + " | "
        html += '<li>{}</li>'.format('<br/> Nome do Artigo: ' + artigo.titulo + "<br/>"+x)

    return HttpResponse(html)

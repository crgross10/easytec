from mainapp.models import NivelCurso
from mainapp.forms import NivelCursoForm

from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.views.decorators.csrf import csrf_exempt

from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from datetime import date, datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
from django.template.loader import render_to_string
from django.utils.formats import get_format

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import authenticate, login, logout

from django.template import RequestContext

from django.core.exceptions import PermissionDenied

from django.contrib import messages

import math

from mail_templated import send_mail
from django.conf import settings
import os
import pandas as pd



import requests


from django.core import serializers
import json

from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView


# ----------------------------------------------
@login_required
def index(request):

    #return redirect('index')
    return render(request, 'mainapp/index.html')





# NivelCurso
# ----------------------------------------------
class NivelCursoListView( LoginRequiredMixin ,  ListView):
    template_name = "mainapp/lista_nivelcurso.html"
    model = NivelCurso
    context_object_name = "nivelcurso"

    def get_queryset(self):
        nivelcursos = NivelCurso.objects.all()
        consulta = self.request.GET.get('pesquisa_nivelcurso')

        if consulta is not None:
            nivelcursos = nivelcursos.filter(nome__icontains=consulta)

        return nivelcursos

class NivelCursoCreateView(LoginRequiredMixin, CreateView):
    template_name = "mainapp/cria_nivelcurso.html"
    model = NivelCurso
    fields = '__all__'
    context_object_name = 'nivelcurso'
    success_url = reverse_lazy("website:lista_nivelcurso")


class NivelCursoUpdateView( LoginRequiredMixin,UpdateView):
    template_name = "mainapp/atualiza_nivelcurso.html"
    model = NivelCurso
    fields = '__all__'
    context_object_name = 'nivelcurso'
    success_url = reverse_lazy("website:lista_nivelcurso")




def do_login(request):
    msg =''
    usuarioInfo =  User.objects.all()
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        email= request.POST.get('email')
        if email is not None:

            usuarioInfo = usuarioInfo.filter(email=email)
            if len(usuarioInfo) > 0:
                u = User.objects.get(email__exact=email)
                password = User.objects.make_random_password()
                u.set_password(password)
                u.save()

                send_mail('registration/email_rec_senha.tpl', {'senha':password, }, 'nao-responda@undergym.com.br', [email])

                msg = 'A nova senha foi enviada com sucesso para o e-mail cadastrado! Verifique seu lixo eletrônico.'

        elif user is not None:
            print('entrou loagr')
            login(request, user)
            return redirect('/index')
        else:
            msg = 'Usuário ou senha inválidos!'

    return render(request,'registration/login.html',{'msg': msg} )

def do_logout(request):
    logout(request)
    return redirect('/accounts/logout')


#listar, criar e atualizar um nivel
@login_required
def ListaNiveisCurso(request, **kwargs):
    niveis_curso = NivelCurso.objects.all()
    cursos = ('Todos','Inglês','Espanhol','Psicologia','Informática','Matemática')
    form= NivelCursoForm()
    if request.method == 'GET':
        filtro =  request.GET.get('pesquisa_curso')

        if filtro == 'Inglês':
            id_curso=1
        elif filtro == 'Espanhol':
            id_curso=2
        elif filtro == 'Psicologia':
            id_curso=3
        elif filtro == 'Informática':
            id_curso=4
        elif filtro == 'Matemática':
            id_curso=5
        else:
            id_curso=0

        if  id_curso!=0:
           niveis_curso = niveis_curso.filter(curso=id_curso)

    if request.method == 'POST':
        id = request.POST.get('id')
        nivel= request.POST.get('nivel')
        ordem= request.POST.get('ordem')
        livro= request.POST.get('livro')
        editora= request.POST.get('editora')
        edicao= request.POST.get('edicao')
        isbn= request.POST.get('isbn')
        ativo= request.POST.get('ativo')
        gera_certificado= request.POST.get('gera_certificado')
        carga_horaria= request.POST.get('carga_horaria')
        iniciante= request.POST.get('iniciante')
        idade_inicial= request.POST.get('idade_inicial')
        idade_final= request.POST.get('idade_final')
        falta_reprova= request.POST.get('falta_reprova')
        nota_reprova= request.POST.get('nota_reprova')
        modalidade= request.POST.get('modalidade')
        curso= request.POST.get('curso')
        font_color= request.POST.get('font_color')
        background= request.POST.get('background')


        if id =='':
            criar_nivelcurso = niveis_curso.create(nivel=nivel,livro=livro,ordem=ordem,editora=editora,edicao=edicao,isbn=isbn,ativo=ativo,gera_certificado=gera_certificado,carga_horaria=carga_horaria, \
                                                   iniciante=iniciante,idade_inicial=idade_inicial,idade_final=idade_final,falta_reprova=falta_reprova,nota_reprova=nota_reprova, modalidade= modalidade, \
                                                   curso=curso,font_color=font_color,backgroud=background)
        else:
            #niveis_curso = niveis_curso.filter(id=id).distinct()
            #print(niveis_curso)
            #for nc in niveis_curso:
            NivelCurso.objects.filter(id = id).update(nivel=nivel,livro=livro,ordem=ordem,editora=editora,edicao=edicao,isbn=isbn,ativo=ativo,gera_certificado=gera_certificado,carga_horaria=carga_horaria, \
                                                   iniciante=iniciante,idade_inicial=idade_inicial,idade_final=idade_final,falta_reprova=falta_reprova,nota_reprova=nota_reprova, modalidade= modalidade, \
                                                   curso=curso,font_color=font_color,backgroud=background)


        return render(request, 'mainapp/lista_nivelcurso.html' , {'cursos': cursos, 'form':form, 'niveis_curso':niveis_curso})

    return render(request, 'mainapp/lista_nivelcurso.html' , {'cursos': cursos, 'form':form, 'niveis_curso':niveis_curso})


@csrf_exempt
def ExcluirNivelCurso (request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nc = NivelCurso.objects.all()
        nc = nc.filter(id = id)
        print(id)

        nc.delete()
        return JsonResponse({"success":"Updated"})




# carrega os dados para edição
class EditarNivelCursoView(APIView):
    parser_class = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        retorno = self.request.data
        id = retorno.get('id')
        nc = NivelCurso.objects.all()
        nc = nc.filter(id = id)
        dados ={}
        for n  in nc:
            dados.update({'id': n.id, 'nivel': n.nivel, 'curso':n.curso , 'ordem':n.ordem, 'livro':n.livro,'editora':n.editora, 'edicao':n.edicao, 'isbn':n.isbn, 'ativo':n.ativo, \
                          'gera_certificado':n.gera_certificado, 'carga_horaria':n.carga_horaria, 'iniciante':n.iniciante,'idade_inicial':n.idade_inicial,'idade_final':n.idade_final, \
                          'falta_reprova':n.falta_reprova,'nota_reprova': n.nota_reprova, 'modalidade':n.modalidade,'font_color':n.font_color,'backgroud':n.backgroud })
        return  HttpResponse(json.dumps(dados), content_type='application/json')



@csrf_exempt
def EditarNivelCurso(self, request):
    if request.method == 'POST':
        retorno = self.request.data
        id = retorno.get('id')
        nc = NivelCurso.objects.all()
        nc = nc.filter(id = id)
        dados ={}
        for n  in nc:
            dados.update({'id': n.id, 'nivel': n.nivel, 'curso':n.curso , 'ordem':n.ordem, 'livro':n.livro,'editora':n.editora, 'edicao':n.edicao, 'isbn':n.isbn, 'ativo':n.ativo, \
                          'gera_certificado':n.gera_certificado, 'carga_horaria':n.carga_horaria, 'iniciante':n.iniciante,'idade_inicial':n.idade_inicial,'idade_final':n.idade_final, \
                          'falta_reprova':n.falta_reprova,'nota_reprova': n.nota_reprova, 'modalidade':n.modalidade,'font_color':n.font_color,'backgroud':n.backgroud })


        return JsonResponse({"data":dados})

from mainapp.views.views import NivelCursoCreateView, NivelCursoListView, EditarNivelCursoView, index, do_login, do_logout, ListaNiveisCurso, ExcluirNivelCurso

from django.conf.urls import url, include

from django.urls import path
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.template.response import TemplateResponse


app_name = 'website'

urlpatterns = [
    # INDEX
    path('index/', index , name="index"),
    path('', index , name="index"),

    path('accounts/login/', do_login, name = "login"),
    path('logout/', do_logout, name = "logout"),
    path('accounts/', include('django.contrib.auth.urls')),


    # Avaliador
    path('nivelcurso/cadastrar', NivelCursoCreateView.as_view(), name="cadastra_nivelcurso"),
    path('nivelcurso/',ListaNiveisCurso , name='lista_nivelcurso'),
    path('nivelcurso_editar/', EditarNivelCursoView.as_view(), name="atualiza_nivelcurso"),
    path('nivelcurso/excluir/', ExcluirNivelCurso, name="deleta_nivelcurso"),


    ]

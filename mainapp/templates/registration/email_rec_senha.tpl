{% extends "mail_templated/base.tpl" %}
{% load static%}

{% block subject %}
Recuperação de senha
{% endblock %}

{% block body %}

{% endblock %}

{% block html %}
<h3>
<br>
<br>
<div style="text-align:center;">
    <p>Olá! </p>
    <p>Esqueceu sua senha? Não tem problema, nós te ajudamos a recuperar!</p>
    <p>Sua nova senha é <strong style="color:red;">{{senha}}</strong></p>
    <p>Agora basta acessar o site e informar sua nova senha!</p>
    <p>Assim fica fácil.</p>
    <br>
    <br>
    <p>Um abraço,</p>
    <p>Equipe Undergym!</p>
    <br>
    <br>
    <br>
    <br>
    </h3>

    <h6> <p>Enviado por Undergym Sistemas</p>
        <p>Fernando Calegari, 187 - Progresso - Bento Gonçalves -RS </p></h6>

</div>


{% endblock %}

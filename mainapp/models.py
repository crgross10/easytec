from django.db import models
from django.utils import timezone



class NivelCurso(models.Model):
    SimNao_Choices = ((0, "Não"),(1, "Sim"))
    Curso_Choices =  ((0, "Inglês"),(1, "Espanhol"),(2, "Psicologia"), (3, "Informática"), (4, "Matemática"), )
    Modalidade_Choices = ((0, "Presencial"),(1, "Ead"))
    Nivel_Choices = ((0, "STARTER"),(1, "1A"),(2, "1B"),(3, "2A"),(4, "2B"))

    id = models.AutoField(primary_key=True)
    curso = models.IntegerField(default=0,null=False,choices=Curso_Choices)
    nivel = models.IntegerField(default=0,null=False,choices=Nivel_Choices)
    ordem = models.IntegerField(default=0,null=False)
    livro =models.CharField(max_length=300,null=False,blank=False)
    editora =  models.CharField(max_length=100,null=False,blank=False)
    edicao = models.CharField(max_length=100,null=False,blank=False)
    isbn = models.CharField(max_length=100,null=False,blank=False)
    ativo = models.IntegerField(default=0,null=False,choices=SimNao_Choices)
    gera_certificado = models.IntegerField(default=0,null=False,choices=SimNao_Choices)
    carga_horaria = models.CharField(max_length=100,null=False,blank=False)
    iniciante = models.IntegerField(default=0,null=False,choices=SimNao_Choices)
    idade_inicial = models.CharField(max_length=100,null=False,blank=False)
    idade_final = models.CharField(max_length=100,null=False,blank=False)
    falta_reprova = models.IntegerField(default=0,null=False,choices=SimNao_Choices)
    nota_reprova = models.IntegerField(default=0,null=False,choices=SimNao_Choices)
    modalidade = models.IntegerField(default=0,null=False,choices=Modalidade_Choices)
    font_color = models.CharField(max_length=100,null=False,blank=False)
    backgroud = models.CharField(max_length=100,null=False,blank=False)

    class Meta:
        ordering = ['curso']
        db_table = 'nivel_curso'

    def __str__(self):
       return  format(self.nivel)

    objects = models.Manager()

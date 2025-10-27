# models.py
from django.db import models
from django.core.validators import FileExtensionValidator
import os

class Cidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ativa = models.BooleanField(default=True)  # Campo para ativar/desativar cidades
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nome}, {self.estado} - {self.pais}"
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ['nome']

class Fotografia(models.Model):  # Considere renomear para "Media"
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    arquivo = models.FileField(upload_to='media/')  # Anteriormente 'imagem'
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ativa = models.BooleanField(default=True)  # Campo para ativar/desativar mídias
    data_upload = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.cidade.nome}"
    
    def is_video(self):
        """Método para verificar se o arquivo é um vídeo"""
        if self.arquivo:
            ext = os.path.splitext(self.arquivo.name)[1].lower()
            return ext in ['.mp4', '.webm', '.ogg']
        return False
    
    def is_image(self):
        """Método para verificar se o arquivo é uma imagem"""
        return not self.is_video()
    
    def get_file_type(self):
        """Retorna o tipo do arquivo"""
        return "video" if self.is_video() else "image"
    
    class Meta:
        verbose_name = "Fotografia"
        verbose_name_plural = "Fotografias"
        ordering = ['-data_upload']
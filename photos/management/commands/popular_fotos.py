# management/commands/popular_fotos.py
# Crie os diretórios: management/ e management/commands/ no seu app
# E adicione arquivos __init__.py vazios em cada um

from django.core.management.base import BaseCommand
from django.core.files import File
from core.models import Cidade, Fotografia
import os

class Command(BaseCommand):
    help = 'Popula o banco de dados com cidades e fotografias de exemplo'
    
    def handle(self, *args, **options):
        # Criar cidades
        cidades_data = [
            {'nome': 'Porto', 'estado': 'Porto', 'pais': 'Portugal'},
            {'nome': 'São Paulo', 'estado': 'SP', 'pais': 'Brasil'},
            {'nome': 'Rio de Janeiro', 'estado': 'RJ', 'pais': 'Brasil'},
            {'nome': 'Lisboa', 'estado': 'Lisboa', 'pais': 'Portugal'},
            {'nome': 'Salvador', 'estado': 'BA', 'pais': 'Brasil'},
            {'nome': 'Brasília', 'estado': 'DF', 'pais': 'Brasil'},
        ]
        
        self.stdout.write('Criando cidades...')
        
        for cidade_data in cidades_data:
            cidade, created = Cidade.objects.get_or_create(
                nome=cidade_data['nome'],
                defaults={
                    'estado': cidade_data['estado'],
                    'pais': cidade_data['pais']
                }
            )
            
            if created:
                self.stdout.write(f'Cidade criada: {cidade.nome}')
            else:
                self.stdout.write(f'Cidade já existe: {cidade.nome}')
        
        # Exemplo de como adicionar fotografias programaticamente
        self.stdout.write('\nPara adicionar fotografias:')
        self.stdout.write('1. Use o Django Admin')
        self.stdout.write('2. Ou adicione através do shell:')
        self.stdout.write('''
from fotografias.models import Cidade, Fotografia
from django.core.files import File

cidade_porto = Cidade.objects.get(nome='Porto')
with open('/caminho/para/sua/foto.jpg', 'rb') as f:
    foto = Fotografia.objects.create(
        titulo='Vista do Porto',
        descricao='Linda vista da cidade do Porto',
        cidade=cidade_porto,
        imagem=File(f, name='porto_vista.jpg')
    )
        ''')
        
        self.stdout.write(self.style.SUCCESS('Comando executado com sucesso!'))


from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.apps import apps
import os

class Command(BaseCommand):
    help = 'Carrega dados iniciais apenas se o banco estiver vazio'

    def handle(self, *args, **options):
        fixture_file = 'fotografias_cloudinary.json'
        
        if not os.path.exists(fixture_file):
            self.stdout.write(self.style.WARNING(f'Arquivo {fixture_file} não encontrado. Pulando...'))
            return
        
        try:
            # Verifica se já existem fotografias no banco
            Fotografia = apps.get_model('core', 'Fotografia')
            
            total_atual = Fotografia.objects.count()
            
            if total_atual > 0:
                self.stdout.write(
                    self.style.WARNING(f'⚠ Banco já possui {total_atual} fotografias. Pulando importação...')
                )
                return
            
            # Carrega os dados
            self.stdout.write(self.style.SUCCESS(f'→ Carregando dados de {fixture_file}...'))
            call_command('loaddata', fixture_file, verbosity=2)
            
            total_carregado = Fotografia.objects.count()
            self.stdout.write(
                self.style.SUCCESS(f'✓ {total_carregado} fotografias carregadas com sucesso!')
            )
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Erro ao carregar dados: {e}'))
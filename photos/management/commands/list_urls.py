from django.core.management.base import BaseCommand
from django.urls import get_resolver

class Command(BaseCommand):
    help = "Lista todas as URLs do projeto"

    def handle(self, *args, **kwargs):
        resolver = get_resolver()
        for pattern in resolver.url_patterns:
            self.list_urls(pattern)

    def list_urls(self, pattern, prefix=''):
        if hasattr(pattern, 'url_patterns'):  # include()
            for subpattern in pattern.url_patterns:
                self.list_urls(subpattern, prefix + str(pattern.pattern))
        else:
            self.stdout.write(f"{prefix}{pattern.pattern} → {pattern.name}")

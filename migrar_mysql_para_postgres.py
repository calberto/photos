import os
import django
import pandas as pd
import mysql.connector

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "photosEuropa.settings")
django.setup()

from core.models import Cidade, Fotografia

# 1. Conexão MySQL
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="carlos",
    password="calberto",
    database="photos"
)

df1 = pd.read_sql("SELECT * FROM core_cidade", mysql_conn)
df2 = pd.read_sql("SELECT * FROM core_fotografia", mysql_conn)

# 2. Inserir no PostgreSQL via Django ORM
for _, row in df1.iterrows():
    Cidade.objects.create(**row.to_dict())

for _, row in df2.iterrows():
    Fotografia.objects.create(**row.to_dict())

print("Migração concluída!")

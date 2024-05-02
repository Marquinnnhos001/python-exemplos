#Formatação de Strings
from datetime import datetime
ano_atual = datetime.now().year
clube = 'corinthians'
ano_fundacao = 1910
campeonatos_mundial = 2
print(f"{clube} possui {campeonatos_mundial} título mundiais.")
print(f"São {ano_atual - ano_fundacao} anos de existencia.")
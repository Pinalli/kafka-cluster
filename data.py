# -*- coding: iso-8859-1 -*-

from datetime import datetime

# Convertendo as datas para objetos datetime
data1 = datetime.strptime("08/01/1988", "%d/%m/%Y")
data2 = datetime.strptime("08/01/2024", "%d/%m/%Y")

# Calculando a diferença em anos
diferenca_anos = data2.year - data1.year

# Imprimindo o resultado
print(f"Diferença em anos entre {data1.strftime('%d/%m/%Y')} e {data2.strftime('%d/%m/%Y')}: {diferenca_anos} anos")

import statistics
import os

os.system('clear') # limpar terminal antes


# 1 - aplicar a média
print(statistics.mean([3, 2, 5, 8, 9]))

# 2 - aplicar mediana
print(statistics.median([1, 2, 3, 5, 8, 9]))

# 3 - aplicar a moda
print(statistics.median([2, 3, 5, 2, 1, 2, 3, 5, 8, 9]))

# 4 - desvio padrão
"""
- Quanto mais próximo do 0 for o desvio padrão,
significa que os dados do conjunto estão menos dispersos
"""
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))
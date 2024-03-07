import math

class Circulo:
  def __init__ (self):
    self.raio = 0
  def calcular_area(self):
    return math.pi * (self.raio**2)
  def calc_circun(self):
    return math.pi*2*self.raio
x = Circulo()
x.raio = int(input('Informe o valor do raio: '))
print(f'Área do círculo = {x.calcular_area():.2f}')
print(f'Circunferência do círculo = {x.calc_circun():.2f}')

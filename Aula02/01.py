class Circulo:
  def __init__ (self):
    self.raio = 0
  def calcular_area(self):
    return 3.14 * (self.raio**2)
  def calc_circun(self):
    return 3.14*2*self.raio
x = Circulo()
x.raio = 3
print(x.calcular_area())
print(x.calc_circun())

class Pila:
  def __init__(self):
      self.lista = []

  def apilar(self, x):
      self.lista.append(x)

  def desapilar(self):
      if len(self.lista) > 0:
          return self.lista.pop()
      else:
        return None
  def puede_desapilar(self):
      return len(self.lista) > 0

class Lampada:
    def __init__(self):
        self.ligada = False
        self.quente = False

class Sala:
    def __init__(self):
        self.lampadas = [Lampada() for _ in range(3)]

    def ligar_interruptor(self, num):
        self.lampadas[num].ligada = True

    def desligar_interruptor(self, num):
        self.lampadas[num].ligada = False
        self.lampadas[num].quente = True

    def verificar_lampadas(self):
        for i, lampada in enumerate(self.lampadas):
            if lampada.ligada:
                print(f"A lâmpada {i+1} está ligada.")
            elif lampada.quente:
                print(f"A lâmpada {i+1} está desligada, mas quente.")
            else:
                print(f"A lâmpada {i+1} está desligada e fria.")

sala = Sala()

sala.ligar_interruptor(0)

sala.desligar_interruptor(0)
sala.ligar_interruptor(1)

sala.verificar_lampadas()

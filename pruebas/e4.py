class Robot:
    def __init__(self):
        self.posicio = [0.0, 0.0]
        self.velocitat = 1.0

    def dalt(self):
        self.posicio[1] += self.velocitat

    def baix(self):
        self.posicio[1] -= self.velocitat

    def dreta(self):
        self.posicio[0] += self.velocitat

    def esquerra(self):
        self.posicio[0] -= self.velocitat

    def accelerar(self):
        if self.velocitat < 10:
            self.velocitat += 0.5

    def disminuir(self):
        if self.velocitat > 0:
            self.velocitat -= 0.5

    def posicio_actual(self):
        print(f"La posició del robot és ({self.posicio[0]}, {self.posicio[1]})")

    def velocitat_actual(self):
        print(f"La velocitat del robot és {self.velocitat}")

robot = Robot()

while True:
    accio = input("> ")

    if accio == "DALT":
        robot.dalt()
    elif accio == "BAIX":
        robot.baix()
    elif accio == "DRETA":
        robot.dreta()
    elif accio == "ESQUERRA":
        robot.esquerra()
    elif accio == "ACCELERAR":
        robot.accelerar()
    elif accio == "DISMINUIR":
        robot.disminuir()
    elif accio == "POSICIO":
        robot.posicio_actual()
    elif accio == "VELOCITAT":
        robot.velocitat_actual()
    elif accio == "END":
        break
    else:
        print("Acció desconeguda")
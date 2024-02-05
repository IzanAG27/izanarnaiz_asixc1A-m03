from time import sleep

# region Declaració de Funcions ----------
def recopilar_ingredients():
    print("Comprar al supermercat")
    sleep(1)
    print("Disposar-los sobre el marbre")
    sleep(1)
    return print("Hecho")


def cuinar_tallarines():
    print("Preparar aigua")
    sleep(1)
    print("Bullir tallarines")
    sleep(1)
    print("Escórrer tallarines")
    sleep(1)
    print("Deixar-les preparades")
    sleep(1)


def cuinar_pastanagues():
    print("Tallar pastanagues")
    sleep(1)
    print("Fregir pastanagues")
    sleep(1)
    print("Deixar pastanagues")
    sleep(1)


def cuinar_cebes():
    print("Tallar cebes")
    sleep(1)
    print("Fregir cebes")
    sleep(1)
    print("Deixar cebes preparades")
    sleep(1)


def preparacio_final():
    print("Barrejar ingredients amb salsa yakitori")
    sleep(1)
    print("Saltar ingredients")
    sleep(1)
    print("Deixar llest per servir")
    sleep(1)


# endregion
# region INICI: Preparar fideus Yakisoba
recopilar_ingredients()
cuinar_tallarines()
cuinar_pastanagues()
cuinar_cebes()
preparacio_final()
# endregion

from time import sleep


# region Declaració de Funcions ----------
def recopilar_ingredients():
    print("Comprar al supermercat")
    sleep(1)
    print("Disposar-los sobre el marbre")
    sleep(1)
    return print("Hecho")


def preparar_aigua():
    print("Escalfar-hi aigua")
    print("Posar-hi sal")


def cuinar_tallarines():
    preparar_aigua()
    sleep(1)
    print("Bullir tallarines")
    sleep(1)
    print("Escórrer tallarines")
    sleep(1)
    print("Deixar-les preparades")
    sleep(1)


def fregir_pastanagues():
    print("Preparar paella per fregir")
    print("Rossejar pastanagues")
    print("Netejar oli de paella")


def cuinar_pastanagues():
    print("Tallar pastanagues")
    sleep(1)
    fregir_pastanagues()
    sleep(1)
    print("Deixar pastanagues")
    sleep(1)


def fregir_cebes():
    print("Preparar paella per fregir")
    print("Rossejar cebes")
    print("Netejar oli de paella")


def cuinar_cebes():
    print("Tallar cebes")
    sleep(1)
    fregir_cebes()
    sleep(1)
    print("Deixar cebes preparades")
    sleep(1)


def saltar_ingredients():
    print("Preparar paella per saltar")
    print("Cuinar remenant ingredients")


def preparacio_final():
    print("Barrejar ingredients amb salsa yakitori")
    sleep(1)
    saltar_ingredients()
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

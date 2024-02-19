llibres = []
num_llibres = int(input())
for _ in range(num_llibres):
    titol = input()
    autor = input()
    pagines = int(input())
    llibres.append({'titol': titol, 'autor': autor, 'pagines': pagines})
print("Llibres\n------------")
for llibre in llibres:
    print(f"{llibre['titol']} - {llibre['autor']} - {llibre['pagines']} pàgines")
print("------------")
print(f"Total: {len(llibres)} llibres")
llibre_mes_curt = min(llibres, key=lambda llibre: llibre['pagines'])
llibre_mes_llarg = max(llibres, key=lambda llibre: llibre['pagines'])
print(f"Llibre més curt: {llibre_mes_curt['titol']} - {llibre_mes_curt['autor']} - {llibre_mes_curt['pagines']} pàgines")
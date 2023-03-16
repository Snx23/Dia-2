print("BIENVENIDO AL CALCULADOR DE PORCENTAJE")
dinero = float(input("Cuanto es el total?: $ "))
prc = int(input("Que porcentaje te gustaria dejar? 10, 12 o 15?: ")) # prc = porcentaje
prs = int(input("Cuantas personas son?: "))                          # prs = personas

formula = dinero * prc/100
redondeo = round((dinero + formula) / prs, 2)               
print(f"Cada persona tendra que pagar ${redondeo}")

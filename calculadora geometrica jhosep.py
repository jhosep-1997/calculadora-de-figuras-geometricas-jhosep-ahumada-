
PI = 3.14159265358979

print("=== CALCULADORA GEOMÉTRICA ===")

def menu_principal():
    print("\n¿Qué tipo de figura quieres calcular?")
    print("1. Figuras 2D")
    print("2. Figuras 3D")
    print("3. Salir")
    return input("Escribe 1, 2 o 3: ").strip()

def menu_calculo_2d():
    print("\n¿Qué quieres calcular?")
    print("1. Área")
    print("2. Perímetro")
    return input("Escribe 1 o 2: ").strip()

def menu_calculo_3d():
    print("\n¿Qué quieres calcular?")
    print("1. Área superficial")
    print("2. Volumen")
    return input("Escribe 1 o 2: ").strip()

def raiz(numero):
    return numero ** 0.5

# ─────────────────── FIGURAS 2D ───────────────────

def triangulo_equilatero():
    lado = float(input("¿Cuánto mide cada lado del triángulo? "))
    calculo = menu_calculo_2d()
    if calculo == "1":
        area = (raiz(3) / 4) * lado ** 2
        print(f"  Área del triángulo equilátero: {area:.2f} u²")
    elif calculo == "2":
        perimetro = lado * 3
        print(f"  Perímetro del triángulo equilátero: {perimetro:.2f} u")
    else:
        print("Opción inválida.")

def triangulo_rectangulo():
    print("\nIngresa los dos lados que conoces y calcularemos el tercero.")
    print("  H = Hipotenusa (el lado más largo, el de enfrente del ángulo recto)")
    print("  O = Cateto Opuesto (el lado de arriba o abajo)")
    print("  A = Cateto Adyacente (el lado del costado)")

    known = input("¿Qué dos lados conoces? Escribe las dos letras juntas (ejemplo: HO, HA u OA): ").upper().strip()

    if "H" in known and "O" in known and "A" not in known:
        H = float(input("  ¿Cuánto mide la hipotenusa? "))
        O = float(input("  ¿Cuánto mide el cateto opuesto? "))
        if H <= O:
            print("Error: la hipotenusa tiene que ser más larga que el cateto opuesto.")
            return
        A = raiz(H**2 - O**2)
        print(f"\n  Cateto adyacente calculado: {A:.2f} u")

    elif "H" in known and "A" in known and "O" not in known:
        H = float(input("  ¿Cuánto mide la hipotenusa? "))
        A = float(input("  ¿Cuánto mide el cateto adyacente? "))
        if H <= A:
            print("Error: la hipotenusa tiene que ser más larga que el cateto adyacente.")
            return
        O = raiz(H**2 - A**2)
        print(f"\n  Cateto opuesto calculado: {O:.2f} u")

    elif "O" in known and "A" in known and "H" not in known:
        O = float(input("  ¿Cuánto mide el cateto opuesto? "))
        A = float(input("  ¿Cuánto mide el cateto adyacente? "))
        H = raiz(O**2 + A**2)
        print(f"\n  Hipotenusa calculada: {H:.2f} u")

    else:
        print("No se reconoció la combinación. Escribe exactamente dos letras: HO, HA u OA.")
        return

    calculo = menu_calculo_2d()
    if calculo == "1":
        area = (O * A) / 2
        print(f"  Área del triángulo rectángulo: {area:.2f} u²")
    elif calculo == "2":
        perimetro = O + A + H
        print(f"  Perímetro del triángulo rectángulo: {perimetro:.2f} u")
        print(f"    Cateto opuesto:    {O:.2f} u")
        print(f"    Cateto adyacente:  {A:.2f} u")
        print(f"    Hipotenusa:        {H:.2f} u")
    else:
        print("Opción inválida.")

def circulo():
    radio = float(input("¿Cuánto mide el radio del círculo? (la mitad del ancho) "))
    calculo = menu_calculo_2d()
    if calculo == "1":
        area = PI * radio ** 2
        print(f"  Área del círculo: {area:.2f} u²")
    elif calculo == "2":
        circunferencia = 2 * PI * radio
        print(f"  Circunferencia del círculo: {circunferencia:.2f} u")
    else:
        print("Opción inválida.")

def rectangulo():
    base   = float(input("¿Cuánto mide el lado de abajo del rectángulo? "))
    altura = float(input("¿Cuánto mide el lado del costado del rectángulo? "))
    calculo = menu_calculo_2d()
    if calculo == "1":
        area = base * altura
        print(f"  Área del rectángulo: {area:.2f} u²")
    elif calculo == "2":
        perimetro = 2 * (base + altura)
        print(f"  Perímetro del rectángulo: {perimetro:.2f} u")
    else:
        print("Opción inválida.")

def figuras_2d():
    print("\n¿Qué figura quieres usar?")
    print("1. Triángulo equilátero")
    print("2. Triángulo rectángulo")
    print("3. Círculo")
    print("4. Rectángulo")
    figura = input("Escribe el número de la figura: ").strip()

    if   figura == "1": triangulo_equilatero()
    elif figura == "2": triangulo_rectangulo()
    elif figura == "3": circulo()
    elif figura == "4": rectangulo()
    else: print("Opción inválida.")

# ─────────────────── FIGURAS 3D ───────────────────

def cubo():
    lado = float(input("¿Cuánto mide un lado del cubo? "))
    calculo = menu_calculo_3d()
    if calculo == "1":
        area = 6 * lado ** 2
        print(f"  Área superficial del cubo: {area:.2f} u²")
    elif calculo == "2":
        volumen = lado ** 3
        print(f"  Volumen del cubo: {volumen:.2f} u³")
    else:
        print("Opción inválida.")

def esfera():
    radio = float(input("¿Cuánto mide el radio de la esfera? (la mitad del ancho) "))
    calculo = menu_calculo_3d()
    if calculo == "1":
        area = 4 * PI * radio ** 2
        print(f"  Área superficial de la esfera: {area:.2f} u²")
    elif calculo == "2":
        volumen = (4 / 3) * PI * radio ** 3
        print(f"  Volumen de la esfera: {volumen:.2f} u³")
    else:
        print("Opción inválida.")

def cilindro():
    radio  = float(input("¿Cuánto mide el radio de la tapa circular? (la mitad del ancho) "))
    altura = float(input("¿Cuánto mide la altura del cilindro? "))
    calculo = menu_calculo_3d()
    if calculo == "1":
        area = 2 * PI * radio * (radio + altura)
        print(f"  Área superficial del cilindro: {area:.2f} u²")
    elif calculo == "2":
        volumen = PI * radio ** 2 * altura
        print(f"  Volumen del cilindro: {volumen:.2f} u³")
    else:
        print("Opción inválida.")

def cono():
    radio  = float(input("¿Cuánto mide el radio de la base del cono? (la mitad del ancho de abajo) "))
    altura = float(input("¿Cuánto mide la altura del cono? (de la base a la punta) "))
    lado_inclinado = raiz(radio**2 + altura**2)
    print(f"  Lado inclinado calculado: {lado_inclinado:.2f} u")
    calculo = menu_calculo_3d()
    if calculo == "1":
        area = PI * radio * (radio + lado_inclinado)
        print(f"  Área superficial del cono: {area:.2f} u²")
    elif calculo == "2":
        volumen = (1 / 3) * PI * radio ** 2 * altura
        print(f"  Volumen del cono: {volumen:.2f} u³")
    else:
        print("Opción inválida.")

def piramide_cuadrada():
    base   = float(input("¿Cuánto mide un lado de la base cuadrada? "))
    altura = float(input("¿Cuánto mide la altura de la pirámide? (de la base a la punta) "))
    lado_triangulo = raiz((base / 2)**2 + altura**2)
    print(f"  Altura de cada cara triangular calculada: {lado_triangulo:.2f} u")
    calculo = menu_calculo_3d()
    if calculo == "1":
        area = base**2 + 2 * base * lado_triangulo
        print(f"  Área superficial de la pirámide: {area:.2f} u²")
    elif calculo == "2":
        volumen = (1 / 3) * base**2 * altura
        print(f"  Volumen de la pirámide: {volumen:.2f} u³")
    else:
        print("Opción inválida.")

def figuras_3d():
    print("\n¿Qué figura quieres usar?")
    print("1. Cubo")
    print("2. Esfera")
    print("3. Cilindro")
    print("4. Cono")
    print("5. Pirámide de base cuadrada")
    figura = input("Escribe el número de la figura: ").strip()

    if   figura == "1": cubo()
    elif figura == "2": esfera()
    elif figura == "3": cilindro()
    elif figura == "4": cono()
    elif figura == "5": piramide_cuadrada()
    else: print("Opción inválida.")

# ─────────────────── BUCLE PRINCIPAL ───────────────────

dimension = ""
while dimension != "3":
    dimension = menu_principal()
    if   dimension == "1": figuras_2d()
    elif dimension == "2": figuras_3d()
    elif dimension == "3": print("\n¡Hasta luego!")
    else: print("Opción inválida, escribe 1, 2 o 3.")
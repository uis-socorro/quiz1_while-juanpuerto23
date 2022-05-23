c1 = int(input("Digite la capital de Pedro: "))
c2 = int(input("Digite la capital de Juan: "))
c3 = int(input("Digite la inversion: "))

meses = 0

while ((c1 + c2) < c3):
    c1 = c1 + (c1 * 0.03)
    c2 = c2 + (c2 * 0.04)
    meses = meses + 1

print("El tiempo para que se pueda hacer la inversión de " + str(c3) + " es de " + str(meses) + " meses.")


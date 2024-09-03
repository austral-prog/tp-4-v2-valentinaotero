def es_bisiesto(leap_year):
    return (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0)

leap_year = int(input("Ingrese un año: "))

if es_bisiesto(leap_year):
    print(f"El año {leap_year} es bisiesto")
else:
    print(f"El año {leap_year} no es bisiesto")


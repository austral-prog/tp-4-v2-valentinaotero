def leap_year():
    leap_year = int(input("Ingrese un año: "))

    is_leap_year = (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0)
    return f"El año {leap_year} {"es" if is_leap_year else "no es"} bisiesto"
    
    is_leap_year = (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0)
    return f"El año {leap_year} es bisiesto" if is_leap_year else f"El año {leap_year} no es bisiesto"
    
    if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
        return f"El año {leap_year} es bisiesto"
    else:
        return f"El año {leap_year} no es bisiesto"


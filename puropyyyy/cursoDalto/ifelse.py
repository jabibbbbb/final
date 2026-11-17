ingreso_mensual = 81000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0: 
        print("estas en defcit")
    elif ingreso_mensual - gasto_mensual > 3000:
        ("bien pa, estas bien")    
    else:
        print("estas gastando mucho, hay que ver si te alcanza")

elif ingreso_mensual > 10000:
    print("estas bien en latinoamerica")

elif ingreso_mensual > 500:
    print("estas bien en argentina")

elif ingreso_mensual > 200:
    print("estas bien en venezuela")                        
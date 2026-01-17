

productos = {}

def crear_producto():

    while True:
        print('-' * 100)
        print('Registrar un Producto')
        print('-' * 100)

        while True:
            nombre_producto = input('\nDigite el Nombre del Producto -> ')
            if len(nombre_producto) >= 2:
                break
            else:
                print('El valor Introducido tiene que tener al menos 2 caracteres')

        while True:
            stock_input = input('Digite el Stock del Producto -> ')
            try:
                if int(stock_input) > 0:
                    stock_producto = str(stock_input)
                    break
                else:
                    print('Digite un Valor Valido (Mayor a 0)')
            except ValueError:
                print('Digite un Valor Valido (Numero Entero)')

        while True:
            opcion = input('Digite la Unidad del Producto (1.Unidades 2.Cajas) -> ')
            if opcion == '1':
                unidad_stock_producto = 'Unidades'
                break
            elif opcion == '2':
                unidad_stock_producto = 'Cajas'
                break
            else:
                print('Por favor digite un Dato Valido')

        while True:    
            modelo_producto = input('Digite el Modelo del Producto -> ')
            if modelo_producto is not None and len(modelo_producto) >= 1:
                break
            else:
                print('-' * 100)
                print('Por Favor Digite al menos un caracter')
                print('-' * 100)

        while True:    
            marca_producto = input('Digite la Marca del Producto -> ')
            if marca_producto is not None and len(marca_producto) >= 1:
                break
            else:
                print('-' * 100)
                print('Por Favor Digite al menos un caracter')
                print('-' * 100)

        while True:    
            fabricante_producto = input('Digite el Nombre del Fabricante del Producto -> ')
            if fabricante_producto is not None and len(fabricante_producto) >= 1:
                break
            else:
                print('-' * 100)
                print('Por Favor Digite al menos un caracter')
                print('-' * 100)

        while True:
            opcion_estado = input('Digite el Estado del Producto (Esciba "1" si desea que este activo o "0" si desea que no este activo) -> ')
            if opcion_estado == '1':
                estado_producto = 'activo'
                break
            elif opcion_estado == '0':
                estado_producto = 'no activo'
                break
            else:
                print('Por favor digite un Dato Valido')
        break

    identificacion_unica = id_unico(modelo_producto, marca_producto, fabricante_producto)
    
    productos[identificacion_unica] = {('id', identificacion_unica), ('nombre', nombre_producto), ('stock', stock_producto), ('unidad_stock', unidad_stock_producto), ('marca', marca_producto), ('modelo', modelo_producto), ('fabricante', fabricante_producto), ('estado', estado_producto)}
    productos[nombre_producto] = {('id', identificacion_unica), ('nombre', nombre_producto), ('stock', stock_producto), ('unidad_stock', unidad_stock_producto), ('marca', marca_producto), ('modelo', modelo_producto), ('fabricante', fabricante_producto), ('estado', estado_producto)}

def obtener_producto():
        
    resultado = 0
    lista_resultados = []

    while True:
        busqueda = input('Digite el Nombre o ID Del Producto Que Desea Buscar -> ')
        if len(busqueda) < 3:
            print('-' * 100)
            print('Por Favor Digite un Dato de al menos 3 DIGITOS')
            print('-' * 100)
        else:
            break

    print('\nResultados:')
    a = 1
    for i in productos:
        if busqueda.lower() in i.lower():
            print(f'{a}.{i}')
            a =+ 1
            resultado += 1
            lista_resultados.append(i)

    if resultado == 0:
        print('No se ha Encontro Ningun Resultado')

    elif resultado >= 1:
        while True:
            try:    
                eleccion = int(input('\nPor favor Digite a Cual Desea Ingresar -> '))
                if int(eleccion) > resultado or int(eleccion) <= 0:
                    print('Por Favor Digite un Valor Valido')
                else:
                    break
            except:
                 print('-' * 100)
                 print('Por Favor Digite un Numero Entero')
                 print('-' * 100)
        
        print('')
        for i in productos[lista_resultados[eleccion - 1]]:
                    print(f'{i}: {productos[lista_resultados[eleccion - 1]].get(i)}') 

def listar_productos():
    pass

def id_unico(modelo, marca, fabricante):
    '''
    Esta funcion hace que cree el ID para el producto para esto:
    #Primero: Tengo que obtener los datos de Marca, Modelo y Fabricante
    #Segundo: Verificar si existen en la base de datos y si es asi obtener el numero asignado de cada uno en caso contrario agregarlo a la tabla y asignarle un numero
    #Tercero: Juntar los 3 numeros para crear el dato
    '''
    #Estas listas son para probar en Python ya que aun no se agrega BD
    #####
    modelo_bd = ['A1','A2','B1','C4']
    marca_bd = ['Samsung']
    fabricante_bd = ['Samsung']
    ####
    modelo_num = None
    marca_num = None
    fabricante_num = None

    for i in modelo_bd:
        if i == modelo:
            modelo_num = '00' + str(modelo_bd.index(i) + 1)
            break
    if modelo_num is None:
        modelo_bd.append(modelo)
        modelo_num = '00' + str(len(modelo_bd))

    for i in marca_bd:
        if i == marca:
            marca_num = '00' + str(marca_bd.index(i) + 1)
            break
    if marca_num is None:
        marca_bd.append(marca)
        marca_num = '00' + str(len(marca_bd))

    for i in fabricante_bd:
        if i == fabricante:
            fabricante_num = '00' + str(fabricante_bd.index(i) + 1)
            break
    if fabricante_num is None:
        fabricante_bd.append(fabricante)
        fabricante_num = '00' + str(len(fabricante_bd))

    return(modelo_num + '-' + marca_num + '-' + fabricante_num)


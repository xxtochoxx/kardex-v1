from sqlalchemy import text, or_
from database import SessionLocal
from tables_db import Producto, Modelo, Marca, Fabricante

def crear_producto():

    while True:
        print()
        print('-' * 80)
        print('Registrar un Producto')
        print('-' * 80)

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
                estado_producto = True
                break
            elif opcion_estado == '0':
                estado_producto = False
                break
            else:
                print('Por favor digite un Dato Valido')
        break

    datos_id = generar_id_unico(marca_producto, modelo_producto, fabricante_producto)
    id = f'{datos_id[0]:03d}-{datos_id[1]:03d}-{datos_id[2]:03d}'

    session = SessionLocal()

    try:
        producto = Producto(
            codigo_producto= id,
            nombre= nombre_producto,
            modelo_id= datos_id[2],
            marca_id= datos_id[1],
            fabricante_id= datos_id[0],
            unidad_stock= unidad_stock_producto,
            stock_actual= int(stock_producto),
            estado= estado_producto
            )
        session.add(producto)
        session.commit()
        print('-' * 80)
        print("✅ Producto insertado correctamente")
        print('-' * 80)
        print()
    except Exception as e:
        session.rollback()
        print("❌ Error al insertar:", e)
    finally: 
        session.close()

def obtener_producto():
    session = SessionLocal()

    while True:
        print()
        print('*' * 80)
        busqueda = input('Digite el Nombre o ID Del Producto Que Desea Buscar -> ')
        print('*' * 80)
        if len(busqueda) < 3:
            print('-' * 100)
            print('Por Favor Digite un Dato de al menos 3 DIGITOS')
            print('-' * 100)
        else:
            break

    productos = session.query(Producto).filter(
        or_(
            Producto.nombre.ilike(f"%{busqueda}%"),
            Producto.codigo_producto.ilike(f"%{busqueda}%")
        )
    ).all()

    if len(productos) == 0:
        print('\nNo se ha Encontrado Ningun Resultado')
    else:
        print()
        print('-' * 80)
        print('Elementos Encontrados:')
        print('-' * 80)
        print('\nCodigo - Nombre - Modelo - Marca - Fabricante - Unidad Stock - Stock Actual - Estado')
        print()

        for producto in productos:
            print(f'{producto.codigo_producto} - {producto.nombre} - {producto.modelo.nombre} - {producto.marca.nombre} - {producto.fabricante.nombre} - {producto.unidad_stock} - {producto.stock_actual} - {producto.estado}')
        print()
    session.close()
    return productos

def listar_productos():
    session = SessionLocal()

    productos = session.query(Producto).all()

    print()
    print('*' * 80)
    print('Elementos Encontrados:')
    print('*' * 80)
    print('\nCodigo - Nombre - Modelo - Marca - Fabricante - Unidad Stock - Stock Actual - Estado')
    print()

    a = 1
    for producto in productos:
        print(f'{a}. {producto.codigo_producto} - {producto.nombre} - {producto.modelo.nombre} - {producto.marca.nombre} - {producto.fabricante.nombre} - {producto.unidad_stock} - {producto.stock_actual} - {producto.estado}')
        a += 1
    
def generar_id_unico(marca, modelo, fabricante) -> str:
    session = SessionLocal()
    id = []
    try:
        query_fabricante = text("SELECT codigo FROM fabricantes WHERE nombre = :fabricante;")
        resultado_fabricante = session.execute(query_fabricante, {'fabricante': fabricante}).fetchone()

        if resultado_fabricante is None:
            query_fabricante = text('SELECT codigo FROM fabricantes ORDER BY "id" DESC LIMIT 1')
            resultado_fabricante = session.execute(query_fabricante).fetchone()
            if resultado_fabricante is None:
                id.append(1)
                fabricante_bd = Fabricante(
                id = id[0],
                nombre = fabricante,
                codigo = '001'
                )
                session.add(fabricante_bd)
                session.commit()
            else:    
                resultado_fabricante = resultado_fabricante[0]
                id.append(int(resultado_fabricante) + 1)
                fabricante_bd = Fabricante(
                id = id[0],
                nombre = fabricante,
                codigo = f'{id[0]:03d}'
                )
                session.add(fabricante_bd)
                session.commit()
        else:
            resultado_fabricante = resultado_fabricante[0]
            id.append(int(resultado_fabricante))

        query_marca = text("SELECT codigo FROM marcas WHERE nombre = :marca;")
        resultado_marca = session.execute(query_marca, {'marca': marca}).fetchone()

        if resultado_marca is None:
            query_marca = text('SELECT codigo FROM marcas ORDER BY "id" DESC LIMIT 1')
            resultado_marca = session.execute(query_marca).fetchone()
            if resultado_marca is None:
                id.append(1)
                marca_bd = Marca(
                id = id[1],
                nombre = marca,
                codigo = '001',
                fabricante_id = id[0]
                )
                session.add(marca_bd)
                session.commit()
            else:
                resultado_marca = resultado_marca[0]
                id.append(int(resultado_marca) + 1)
                marca_bd = Marca(
                id = id[1],
                nombre = marca,
                codigo = f'{id[1]:03d}',
                fabricante_id = id[0]
                )
                session.add(marca_bd)
                session.commit()
        else:
            resultado_marca = resultado_marca[0]
            id.append(int(resultado_marca))

        query_modelo = text("SELECT codigo FROM modelos WHERE nombre = :modelo;")
        resultado_modelo = session.execute(query_modelo, {'modelo': modelo}).fetchone()

        if resultado_modelo is None:
            query_modelo = text('SELECT codigo FROM modelos ORDER BY "id" DESC LIMIT 1')
            resultado_modelo = session.execute(query_modelo).fetchone()
            if resultado_modelo is None:
                id.append(1)
                modelo_bd = Modelo(
                id = id[2],
                nombre = modelo,
                codigo = '001',
                marca_id = id[1]
                )
                session.add(modelo_bd)
                session.commit()
            else:
                resultado_modelo = resultado_modelo[0]
                id.append(int(resultado_modelo) + 1)
                modelo_bd = Modelo(
                id = id[2],
                nombre = modelo,
                codigo = f'{id[2]:03d}',
                marca_id = id[1]
                )
                session.add(modelo_bd)
                session.commit()
        else:
            resultado_modelo = resultado_modelo[0]
            id.append(int(resultado_modelo))

    finally:
        session.close()

    return(id)

while True:
    print('°' * 80)
    print('Menu de Funciones del Kardex:')
    print('°' * 80)
    print()
    print('1. Crear Producto')
    print('2. Obtener Producto')
    print('3. Listar Productos')
    print('\nDigite "Exit" para Salir')
    funcion = input('\nPor favor Digite que Funcion Desea Usar -> ')

    if funcion == '1':
        crear_producto()
    elif funcion == '2':
        obtener_producto()
    elif funcion == '3':
        listar_productos()
    elif funcion.lower() == 'exit':
        break
    else:
        print('-' * 80)
        print('Digite un Valor Valido Por Favor')
        print('-' * 80)

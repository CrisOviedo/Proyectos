import csv
import os
import sys

clients = []
CLIENT_TABLE = ".clients.csv"
CLIENT_SCHEMA = ['nombre','cedula', 'correo', 'telefono',]

products = []
PRODUCT_TABLE = ".products.csv"
PRODUCT_SCHEMA = ['nombre', 'codigo', 'cantidad']


def _initialize_clients_from_storage():
	with open(CLIENT_TABLE,mode='r') as f:
		reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)

		for row in reader:
			clients.append(row)

def _initialize_product_from_storage():
	with open(PRODUCT_TABLE,mode='r') as f:
		reader = csv.DictReader(f,fieldnames=PRODUCT_SCHEMA)

		for row in reader:
			products.append(row)


def _save_clients_to_storage():
	tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
	with open(tmp_table_name,mode='w') as f:
		writer = csv.DictWriter(f,fieldnames=CLIENT_SCHEMA)
		writer.writerows(clients)

	os.remove(CLIENT_TABLE)
	os.rename(tmp_table_name,CLIENT_TABLE)


def _save_product_to_storage():
	tmp_table_name = '{}.tmp'.format(PRODUCT_TABLE)
	with open(tmp_table_name,mode='w') as f:
		writer = csv.DictWriter(f,fieldnames=PRODUCT_SCHEMA)
		writer.writerows(products)

	os.remove(PRODUCT_TABLE)
	os.rename(tmp_table_name,PRODUCT_TABLE)


def create_client(client):
	global clients

	if client['cedula'] not in clients:
		clients.append(client)
	else:
		print("El cliente se encuentra registrado")


def create_product(product):
    global products

    if product not in products:
        products.append(product)
    else:
        print("El producto se encuentra registrado")


def list_clients():
	print("| NOMBRE | CEDULA | CORREO |	TELEFONO | ")
	for idx, client in enumerate(clients):
		print(f"{idx} │ {client['nombre']} │ {client['cedula']} │ {client['correo']} │ {client['telefono']} │ ")


def list_products():
	print("| NOMBRE | CODIGO | CANTIDAD | ")
	for idx, product in enumerate(products):
		print(f"{idx} │ {product['nombre']} │ {product['codigo']} │ {product['cantidad']} ")


def update_client(cedula):
    global clients

    for client in clients:
        if client['cedula'] == cedula:
            client_new = _input_dic_client()
            client.update(client_new)
            return

    print("No se encontro el cliente")


def update_product(codigo):
    global products

    for product in products:
        if product['codigo'] == codigo:
            product_new = _input_dic_product()
            product.update(product_new)
            return

    print("No se encontro el cliente")


def delete_client(cedula):
    global clients

    for client in clients:
        if client['cedula'] == cedula:
            clients.remove(client)
            print("El cliente fue eliminado correctamente")
            return
    print("No se encontro el cliente")

def delete_product(codigo):
    global products

    for product in products:
        if product['codigo'] == codigo:
            products.remove(product)
            print("El producto fue eliminado correctamente")
            return
    print("No se encontro el producto")


def serch_client(cedula):

	for client in clients:
		if client['cedula'] == cedula:
			print("| NOMBRE | CEDULA | CORREO |	TELEFONO | ")
			print(f"{client['nombre']} │ {client['cedula']} │ {client['correo']} │ {client['telefono']} │ ")

			return True

	print(f"No se encontro {codigo}")
	return False


def serch_product(codigo):

	for product in products:
		if product['codigo'] == codigo:
			print("| NOMBRE | CEDULA | CORREO |	TELEFONO | ")
			print(f"{product['nombre']} │ {product['codigo']} │ {product['cantidad']} │ ")

			return True

	print(f"No se encontro {codigo}")
	return False


def _input_dic_client():

    client = {
        "nombre" : _message_get_input_client("nombre"),
        "cedula" : _message_get_input_client("cedula"),
        "correo" : _message_get_input_client("correo"),
        "telefono" : _message_get_input_client("telefono"),
    }
    return client


def _input_dic_product():

    products = {
        "nombre" : _message_get_input_client("nombre"),
        "codigo" : _message_get_input_client("codigo"),
        "cantidad" : _message_get_input_client("cantidad"),
    }
    return products


def _message_get_input_client(idx):
    message = None

    while not message:
        message = input(f"Ingrese el/la {idx} ").upper()

    return message


def _message_in_not_client():
    print("El cliente no se encuentra en la lista")


def report_product():

	for product in products:
		cantidad = int(product['cantidad'])
		if cantidad < 2:
			print("| NOMBRE | CEDULA | CORREO |	TELEFONO | ")
			print(f"{product['nombre']} │ {product['codigo']} │ {product['cantidad']} │ ")


def intro_menu():
	print("*" * 100)
	print("Bienvenido a Ivensoft")
	print("MENU PRINCIPAL")
	print("Ingrese el comando deseado")
	print("[C]lientes")
	print("[I]nventario")
	print("[R]eporte bodega")
	print("[S]alir")
	print("*" * 100)

	comman = input().upper()

	if comman == "C":
		intro_comman_clients()
	elif comman == "I":
		intro_comman_inventory()
	elif comman == "R":
		report_product()
		intro_menu()
	elif comman == "S":
		_exit()
	else:
		print("Comando invalido")
		intro_menu()


def intro_comman_clients():
	print("*" * 100)
	print("MENU CLIENTES")
	print("Ingrese el comando deseado")
	print("[C]rear cliente")
	print("[E]eliminar cliente")
	print("[A]ctualizar cliente")
	print("[L]istar cliente")
	print("[B]uscar cliente")
	print("[V]olver al menu principal")
	print("[S]alir")
	print("*" * 100)

	comman = input().upper()

	if comman=="C":
		client = _input_dic_client()
		create_client(client)
		intro_comman_clients()
	elif comman=="L":
		list_clients()
		intro_comman_clients()
	elif comman=="E":
		cedula = input("Ingrese cedula del cliente ")
		delete_client(cedula)
		intro_comman_clients()
	elif comman=="A":
		cedula = input("Ingrese cedula del cliente ")
		update_client(cedula)
		intro_comman_clients()
	elif comman=="B":
		cedula = input("Ingrese cedula del cliente ")
		serch_client(cedula)
		intro_comman_clients()
	elif comman=="S":
		_exit()
	elif comman == "V":
		intro_menu()
	else:
		print("Comando invalido")
		intro_comman_clients()

def intro_comman_inventory():
	print("*" * 100)
	print("MENU PRODUCTOS")
	print("Ingrese el comando deseado")
	print("[C]rear producto")
	print("[E]eliminar producto")
	print("[A]ctualizar producto")
	print("[L]istar productos")
	print("[B]uscar producto")
	print("[V]olver al menu principal")
	print("[S]alir")
	print("*" * 100)

	comman = input().upper()

	if comman == "C":
		product = _input_dic_product()
		create_product(product)
		intro_comman_inventory()
	elif comman=="L":
		list_products()
		intro_comman_inventory()
	elif comman=="E":
		codigo = input("Ingrese codigo del producto ").upper()
		delete_product(codigo)
		intro_comman_inventory()
	elif comman=="A":
			codigo = input("Ingrese codigo del producto ").upper()
			update_product(codigo)
			intro_comman_inventory()
	elif comman=="B":
		codigo = input("Ingrese codigo del producto ").upper()
		serch_product(codigo)
		intro_comman_inventory()
	elif comman=="S":
		_exit()
	elif comman == "V":
		intro_menu()
	else:
		print("Comando invalido")
		intro_comman_clients()


def _exit():
	_save_product_to_storage()
	_save_clients_to_storage()
	sys.exit()


if __name__ == '__main__':

	_initialize_product_from_storage()
	_initialize_clients_from_storage()
	intro_menu()

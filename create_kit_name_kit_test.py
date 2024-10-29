import sender_stand_request
import data
from data import user_body, no_name


# Función para cambiar el valor del parámetro firstName en el cuerpo de la solicitud
def get_kit_body(name):
    current_body = data.kit_body.copy() # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body["name"] = name # Se cambia el valor del parámetro firstName
    return current_body # Se devuelve un nuevo diccionario con el valor firstName requerido

# Función de prueba positiva
def positive_assert(name):
    kit_body = get_kit_body(name)# El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    user_response = sender_stand_request.post_new_client_kit(data.kit_body) # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    assert user_response.status_code == 201 # Comprueba si el código de estado es 201

# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_symbol(name):
    kit_body = get_kit_body(name)  # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    user_response = sender_stand_request.post_new_client_kit(kit_body)  # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    assert user_response.status_code == 400# Comprueba si el código de estado es 400
    assert user_response.json()["code"] == 400# Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert user_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

#Prueba 1
# El número permitido de caracteres (1): kit_body = { "name": "a"}
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data._1_letter_in_name)

# El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data._511_letter_in_name)

# El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_symbol(data._0_letter_in_name)

# El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_symbol(data._512_letter_in_name)

# Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert(data.special_symbol)

# Se permiten espacios: kit_body = { "name": " A Aaa " }
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert(data.english_letter_in_name)

# 	Se permiten números: kit_body = { "name": "123" }
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert(data.number_in_name)

# El parámetro no se pasa en la solicitud: kit_body = { }
def test_create_kit_empty_name_get_error_response():
    negative_assert_symbol(data.no_name)

# 	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
def test_create_kit_number_type_name_get_error_response():
    negative_assert_symbol(data.number_type)
import sender_stand_request
import data

# Función para cambiar el valor del parámetro firstName en el cuerpo de la solicitud
def get_kit_body(name):
    current_body = data.kit_body.copy() # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body["name"] = name # Se cambia el valor del parámetro firstName
    return current_body # Se devuelve un nuevo diccionario con el valor firstName requerido

# Función de prueba positiva
def positive_assert(name):
    kit_body = get_kit_body(name)# El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_response = sender_stand_request.post_new_client_kit(kit_body,auth_token) # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    assert user_response.status_code == 201 # Comprueba si el código de estado es 201
    assert user_response.json()["authToken"] != "" # Comprueba que el campo authToken está en la respuesta y contiene un valor
    users_table_response = sender_stand_request.get_users_table() # Comprobar que el resultado de la solicitud se guarda en users_table_response
    # String que debe estar en el cuerpo de respuesta
    str_user = user_body["name"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1

# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_symbol(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(name)
    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  "\
                                         "los nombres deben tener al menos 2 caracteres y no más de 15 caracteres"

# Función de prueba negativa cuando el error es "No se enviaron todos los parámetros requeridos"
def negative_assert_no_firstname(user_body):
    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"
'''
# Prueba 1. Usuario o usuaria creada con éxito. El parámetro firstName contiene 2 caracteres
def test_create_user_2_letter_in_name_get_success_response():
    positive_assert("Aa")

# Prueba 2. Usuario o usuaria creada con éxito. El parámetro firstName contiene 15 caracteres
def test_create_user_15_letter_in_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

# Prueba 3. Error. El parámetro firstName contiene 1 carácter
def test_create_user_1_letter_in_name_get_error_response():
    negative_assert_symbol("A")

# Prueba 4. Error. El parámetro firstName contiene 16 caracteres
def test_create_user_16_letter_in_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")
'''
# Prueba 5. Usuario o usuaria creada con éxito. El parámetro firstName contiene caracteres latinos
def test_create_user_english_letter_in_name_get_success_response():
    positive_assert("A Aaa")
'''
# Prueba 6. Error. El parámetro firstName contiene un string de caracteres especiales
def test_create_user_has_special_symbol_in_name_get_error_response():
    negative_assert_symbol("\"№%@\",")

# Prueba 7. Error. El parámetro firstName contiene un string de dígitos
def test_create_user_has_number_in_name_get_error_response():
    negative_assert_symbol("123")

# Prueba 8. Error. Falta el parámetro firstName en la solicitud
def test_create_user_no_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    user_body = data.user_body.copy()
    # El parámetro "name" se elimina de la solicitud
    user_body.pop("name")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)

# Prueba 9. Error. El parámetro contiene un string vacío
def test_create_user_empty_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body("")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)

# Prueba 10. Error. El tipo del parámetro firstName: número
def test_create_user_number_type_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(12)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400
'''

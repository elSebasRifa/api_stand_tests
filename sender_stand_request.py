import configuration
import requests
import data

def post_new_user(user_body):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, # Concatenación de URL base y ruta.
                         json=user_body, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.

def get_users_table(user_body):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH, # Concatenación de URL base y ruta.
                         json=user_body, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.


response = post_new_user(data.user_body);
print(response.status_code)
print(response.json()) # Muestra del resultado en la consola
response_1 = get_users_table(data.user_body);
print(response_1.status_code)
print(response_1.json()) # Muestra del resultado en la consola
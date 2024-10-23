import configuration
import requests
import data


def post_new_user(user_body):
    # Envía una solicitud para crear un nuevo usuario o usuaria y recuerda el token de autenticación (authToken).
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.

def post_new_client_kit(kit_body,auth_token):
    # Envía una solicitud para crear un kit personal para este usuario o usuaria. Asegúrate de pasar también el encabezado Autorization
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json = kit_body,  # Datos a enviar en la solicitud.
                         headers = auth_token)  # Encabezados de solicitud.

def post(user_body):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, # Concatenación de URL base y ruta.
                         json=user_body, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

response_1 = post_new_client_kit(data.kit_body,data.headers);
print(response_1.status_code)
print(response_1.json())

import configuration
import requests
import data


def post_new_user(user_body):
    # Envía una solicitud para crear un nuevo usuario o usuaria y recuerda el token de autenticación (authToken).
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.


def post_new_client_kit(kit_body):
    headers = data.headers.copy()
    auth_token = post_new_user(data.user_body)
    headers["Authorization"] = f"Bearer {auth_token}"

    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                             json=kit_body,
                             headers=headers)

    return response

def get_users_table(user_body):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH, # Concatenación de URL base y ruta.
                         json=user_body, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())

response_1 = post_new_client_kit(data.kit_body,data.headers);
print(response_1.status_code)
print(response_1.json())

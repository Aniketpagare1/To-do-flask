from keycloak import KeycloakOpenID
from flask import request, abort
from utils import extract_token_from_header

keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:8080/auth/",
    client_id="realm-management",
    realm_name="my-realm",
    client_secret_key="sAa7ssIVZce5k3BrZPxczNLmXS9qOfXA"
)

def keycloak_middleware(request):
    token = extract_token_from_header()
    if token:
        try:
            keycloak_openid.introspect(token)
        except Exception:
            abort(401, description="Unauthorized: Invalid token")
    else:
        abort(401, description="Unauthorized: No token provided")

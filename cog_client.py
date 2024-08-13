# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:52:20 2021

@author: KaranRajagopalan
"""

from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import Token
from msal import PublicClientApplication

# %% QUANTA DETAILS

TENANT_ID = "92bce3bb-abfb-484b-b074-32e1a37f3631"
CLIENT_ID = "cac76024-22d7-4692-9d51-76b5d52f4c8d"
CDF_CLUSTER = "api"  # api, westeurope-1 etc
COGNITE_PROJECT = "susana"
#CACHE_FILENAME = COGNITE_PROJECT + ".bin"

BASE_URL = f"https://{CDF_CLUSTER}.cognitedata.com"
SCOPES = [f"https://{CDF_CLUSTER}.cognitedata.com/.default"]

AUTHORITY_HOST_URI = "https://login.microsoftonline.com"
AUTHORITY_URI = AUTHORITY_HOST_URI + "/" + TENANT_ID
PORT = 53000

def authenticate_azure():

    app = PublicClientApplication(client_id=CLIENT_ID, authority=AUTHORITY_URI)

    # interactive login - make sure you have http://localhost:port in Redirect URI in App Registration as type "Mobile and desktop applications"
    creds = app.acquire_token_interactive(scopes=SCOPES, port=PORT)
    return creds


creds = authenticate_azure()

# def get_client():
#     client = CogniteClient(
#         project=COGNITE_PROJECT,
#         base_url=f"https://{CDF_CLUSTER}.cognitedata.com",
#         client_name="cognite-python-dev",
#         debug=False
#     )
#     return client


cnf = ClientConfig(client_name="my-special-client", project=COGNITE_PROJECT, credentials=Token(creds["access_token"]), base_url=BASE_URL)
client = CogniteClient(cnf)





############ Include these lines below in your code ############
# from cog_client import get_client
# client = get_client() 
#################################################################

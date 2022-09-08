import sys
import requests
import json
import hmac
import hashlib
import base64

server_url = "https://sol-portal-r1.dmsdigital.net"
community_id = "AUTOPAS"
CustomerId = "alejandro.fernandez@autopasion.com.mx"
PartnerId = "AUTOPAS1"
Password = "AutoPas1on"
RooftopId = "SO10TO"
SharedKey = "5cb371b4-4319-4657-9c8c-e8f1d64b35e0"
Version = "1"
hashhhh = "Um9vZnRvcElkPVNPMTBUTzpUb2tlbj03NzlkY2I4Yi1jNWMwLTQ5NDctOGMwOS03NmM0M2JjNWQ2ODE6SGFzaD05M2UzZWU1NzdjNjY3YWNlOTRjM2E5YTY0ZjhiZWU1MzM0NjNhNmJmMGQ2YmMzMmVlYjI4ZGU5YjFlOWE5Zjk0MGJmZTBjMjI0YjcyYzZlYzc4MWVhYThjNmJlMDg1NzA="


def get_token():
    auth_server_url = "{}/api/{}/ServiceOnline/RequestToken".format(server_url, community_id)
    token_req_payload = {
        'CustomerId': CustomerId, 'PartnerId': PartnerId, 'Version': Version, 'CommunityId': community_id
    }

    token_response = requests.post(auth_server_url,
                                   data=token_req_payload)

    if token_response.status_code != 200:
        print("token failed", file=sys.stderr)
    else:
        print("successful token")
        tokens = json.loads(token_response.text)
        token = tokens["Token"]
        return token


def get_password(token_hashed):
    auth = {'Authorization': "DataHub-Hash {}".format(token_hashed)}
    token_req_payload = {'RooftopId': RooftopId}
    url = "{}/api/{}/ServiceOnline/CheckPassword".format(server_url, community_id)
    password_response = requests.post(url,
                                      headers=auth,
                                      data=token_req_payload
                                      )
    if password_response.status_code != 200:
        print("password failed", file=sys.stderr)
    else:
        print("successful Password")
        password = json.loads(password_response.text)
        return password[""]

def get_customers(token_hashed):
    auth = {'Authorization':"DataHub-Token {}".format(token_hashed)}
    token_req_payload = {'CustomerID': CustomerId}
    url = "{}/api/{}/ServiceOnline/GetCustomerInformation".format(server_url, community_id)
    customer_response = requests.post(url,
                                      headers=auth,
                                      data=token_req_payload
                                      )
    if customer_response.status_code != 200:
        print("Customer failed", file=sys.stderr)
    else:
        print("successful Customer")
        password = json.loads(customer_response.text)
        return password[""]

def activation(token_hashed):
    auth = {'Authorisation':"Hash {}".format(token_hashed)}
    token_req_payload = {'Hash': token_hashed}
    url = "{}/api/{}/ServiceOnline/ActivateToken".format(server_url, community_id)
    activation_response = requests.post(url,
                                        headers=auth

                                      )
    if activation_response.status_code != 200:
        print("Customer failed", file=sys.stderr)
    else:
        print("successful Customer")
        password = json.loads(activation_response.text)
        return password[""]

#hashT = get_token()
#print(hashT)
#get_password(hashhhh)
#get_customers(hashhhh)
activation(hashhhh)


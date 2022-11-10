from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os

load_dotenv()

# grabbing env credentials
api_key = os.getenv('API_KEY')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# sending user to authorize
base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://joeymucciaccio.github.io/"
token_url = "https://www.bungie.net/platform/app/oauth/token/"

# community bungie api site for /User/GetCurrentBungieNetUser/
get_user_details_endpoint = "https://www.bungie.net/Platform/User/GetCurrentBungieNetUser/"

# creating session
session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

auth_link = session.authorization_url(base_auth_url)
print(f"Auth link: {auth_link[0]}")

# store reposnse if above process is successful
redirect_response = input("Paste your redirect URL with query parameters here...")

# parse the url (from above) and exchange it for a token
# if method completed successfully, our session object will now have a token inside of it
# Any requests made after this needing a token, it will already include it into those requests
session.fetch_token(
    client_id = client_id,
    client_secret = client_secret,
    token_url = token_url,
    authorization_response = redirect_response
)

# when above is successful, additional headers used to make request
additional_headers = { 'X-API-KEY': os.getenv('API_KEY')}
# save request in a response
response = session.get(url=get_user_details_endpoint, headers=additional_headers)

print(f"RESPONSE STATUS: {response.status_code}")
print(f"RESPONSE REASON: {response.reason}")
print(f"RESPONSE TEXT: \n{response.text}")
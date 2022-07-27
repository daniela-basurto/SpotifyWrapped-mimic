# import requests
# import os

# # CLIENT_ID = 'add keys'
# # CLIENT_SECRET = 'Add keys'

# CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
# CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')



# AUTH_URL = 'https://accounts.spotify.com/api/token'

# # auth_response = requests.post(AUTH_URL, {
# #     'grant_type': 'client_credentials',
# #     'client_id': CLIENT_ID,
# #     'client_secret': CLIENT_SECRET,
# # })


# auth_response = requests.post(AUTH_URL, {
# 'grant_type': 'client_credentials',
# 'client_id': os.environ.get('SPOTIFY_CLIENT_ID'),
# 'client_secret': os.environ.get('SPOTIFY_CLIENT_SECRET'),
# })

# print(auth_response.status_code)

# auth_response_data = auth_response.json()

# access_token = auth_response_data['access_token']

# headers = {
#   'Authorization': 'Bearer {token}'.format(token=access_token)
#   }

# print(auth_response_data)







# # BASE_URL = 'https://api.spotify.com/v1/recommendations'
# # track_id = input('Enter track id: ')  
# # # track_id is the last part of the url when looking for a song
# # r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
# # print(r.json())



# # add functionalities
# # BASE_URL = 'https://api.spotify.com/v1/recommendations'

# # for i in range(5):
# #   track_id = input('Enter track id: ')  
# # # track_id is the last part of the url when looking for a song
# #   r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
# # print(r.json())

################ REDO CODE ABOVE ###################
import requests
# import os

CLIENT_ID = 'add keys'
CLIENT_SECRET = 'add keys'

# CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
# CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# auth_response = requests.post(AUTH_URL, {
# 'grant_type': 'client_credentials',
# 'client_id': os.environ.get('SPOTIFY_CLIENT_ID'),
# 'client_secret': os.environ.get('SPOTIFY_CLIENT_SECRET'),
# })

print(auth_response.status_code)

auth_response_data = auth_response.json()

print(auth_response_data)

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'
track_id = input('Enter track id: ')
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
r = r.json()
print(r)


###### LET USER ENTER 5 TRACK ID ########
# BASE_URL = 'https://api.spotify.com/v1/recommendations'
# for i in range(5):
#   track_id = input('Enter track id: ')  
# # track_id is the last part of the url when looking for a song
#   r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
#   r = r.json()
# print(r)

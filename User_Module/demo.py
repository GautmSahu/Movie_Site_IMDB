import requests

querystring="intersteller"
url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/"

headers = {
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    'x-rapidapi-key': "83606917f9msh6544cdfbd9b7104p1c694fjsn04e02b46f998"
    }

response = requests.request("GET", url+querystring, headers=headers)

print(url+querystring)
print(response.text)


# import requests
#
# url = "https://imdb-api1.p.rapidapi.com/Title/k_12345678/tt1375666"
#
# headers = {
#     'x-rapidapi-host': "imdb-api1.p.rapidapi.com",
#     'x-rapidapi-key': "83606917f9msh6544cdfbd9b7104p1c694fjsn04e02b46f998"
#     }
#
# response = requests.request("GET", url, headers=headers)
#
# print(response.text)
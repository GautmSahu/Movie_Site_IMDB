import requests
res=requests.get("https://www.imdb.com/video/vi1044495385?playlistId=tt9052870&ref_=tt_ov_vi")
print(res.text)
originalurl="https://imdb-video.media-imdb.com/vi2048898073/1434659607842-pgv4ql-1565457462731.mp4?Expires=1596183523&Signature=qR01gtp5LtogKKR24PniBPNZxHZZe2kqEFNUmryU9QMGQARWWeRLLCYlBQh5gcVhsytba4N3rQzwACNVV9z76Arn~E1gsbawhecTf~7kyGhguxukIzqFoRQvR26x1UaIoyLrmHv1lNmhNb4bXYKP6rw4RYu7DRxZrGuyi~GES~suaTYyOqH01rcWOs31VYNeyRMx6MWWm9VbOM7GgD8YiCCf0yDs9h9fmyBwcqkvtC1zZnPsqKivmJG-si4gw1XTNmlU8PGOpfwrutVBgKzM-0vJ9s8GlYOOn9DJVHOCulTDsLK8CYXzTB59ytmgNDXPFCZnqM2KiLrmsZTTUYzgWQ__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA"
textfile_url="https://imdb-video.media-imdb.com/vi1044495385/1434659607842-pgv4ql-1565457462731.mp4?Expires=1596170904&Signature=mRgBx~w~BgVoEt8vRtL9m3zs6bSKbccm-OdbhqKd1vYeIs7CT5cLLrDHuKT29JP3fezjcDTBkyLYfiM4XUbqxOgy3qDWfEvWa9FsRCDJpQYhB~eMvpegfyJehvBvIcvvLZFeq9GH6aVAqid5EzP6M7ufx5vYTc1xF71qve25GqBiqyhau-7Ww3AG3R6KyuEMam6vSilkeY757YpdmhOIzjUWkOWYqz8nGGVnwtK9Zqt0BZPwH0KRyQ0wj5ocO~0hED5yAQpRhQaMnGnc2DYGIcdouWCYmBMOGKPEiXXE~ZZt4Lyp4JeuSG~2zF~cxuircK-RC-H5hGDk7xBm4FdGtQ__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA"







# import requests
#
# querystring="intersteller"
# url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/"
#
# headers = {
#     'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
#     'x-rapidapi-key': "83606917f9msh6544cdfbd9b7104p1c694fjsn04e02b46f998"
#     }
#
# response = requests.request("GET", url+querystring, headers=headers)
#
# print(url+querystring)
# print(response.text)


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
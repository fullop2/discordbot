import urllib.request

lolApiKey = "?api_key=RGAPI-e37fe8bf-60ec-4661-a787-8a00593628d3"
lolApiUrl = "https://kr.api.riotgames.com/"

# request URL
def UrlRequest(dataType, key):
    byte_data = urllib.request.urlopen(lolApiUrl + str(dataType) + str(key) + lolApiKey).read()
    text_data = byte_data.decode('utf-8')
    return text_data

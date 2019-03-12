import urllib.request
import os
lolApiKey = os.environ['LOL_TOKEN']
lolApiUrl = "https://kr.api.riotgames.com/"

# request URL
def UrlRequest(dataType, key):
    byte_data = urllib.request.urlopen(lolApiUrl + str(dataType) + str(key) + lolApiKey).read()
    text_data = byte_data.decode('utf-8')
    return text_data

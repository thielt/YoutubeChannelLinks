from googleapiclient.discovery import build
import json
import pandas as pd
import creds

yt = build('youtube', 'v3', developerKey=creds.api_key)
req = yt.channels().list(
    part='id, statistics, snippet',
    forUsername='nprmusic'  # sample username from schafer
)
res = req.execute()
#print(res)
#print(json.dumps(res, indent=0)) 
#this does organization in json format

user_username = input()
def getID(yt, forUsername):
    req = yt.channels().list(
        part='id, statistics, snippet',
        forUsername=user_username  # sample username from schafer
    )
    res = req.execute()
    for item in res['items']:
        new_id = item['id']
    return new_id

#new_channelID = getID(yt, user_username) #extension on the URL
#print(new_channelID)

def getVideosId(youtube, channelId):
    videosIdList = []
    nextPageToken = None

    while True:
        request = youtube.search().list(
            part="snippet",
            channelId=channelId,
            maxResults=100,
            regionCode='US',
            pageToken=nextPageToken,
        )
        response = request.execute()

        for item in response['items']:
            if item['id']['kind'] == "youtube#video":
                videosIdList.append(item['id']['videoId'])

        nextPageToken = response.get('nextPageToken')
        if not nextPageToken:
            break

    return videosIdList

print('Enter Username to show all links to Videos and channel info: ')
user_username = input()
list_vids = getVideosId(yt, getID(yt, user_username))

links = []
for ids in list_vids:
    newlink = 'https://www.youtube.com/watch?v=' + ids
    links.append(newlink)
chart = pd.DataFrame(links)
print(chart)
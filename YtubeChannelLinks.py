#github
#https://github.com/zakicode19/YouTubeApi/blob/main/youtube_api.ipynb

#https://www.youtube.com/watch?v=coZbOM6E47I&t=16s
#Calculating duration of a playlist

#https://www.youtube.com/watch?v=th5_9woFJmk&t=2s
#Creating an API Key and Querying the API

# API KEY
#AIzaSyC2u-1TGLLVih-QMyW34vCM45UI4nUWej0

# google api python client
#https://github.com/googleapis/google-api-python-client
#show installation

#youtube api
#https://developers.google.com/youtube/v3

#search id
#channels.list(part="id", forUsername="username") or
#search.list(part="snippet", type="channel", q="display name")

from googleapiclient.discovery import build
import json
import pandas as pd


#secret key file needed
api_key = ''

#creating service object to access API Key
yt = build('youtube', 'v3', developerKey = api_key)

#via docs, channel > list > part function
req = yt.channels().list(
    part = 'id, statistics, snippet',
    forUsername = 'nprmusic'   #sample username from schafer
)

#store id for input using forUsername and id>items
'''
req1 = yt.search().list(
    part = 'snippet',
    type = 'channel',
    q = 'npr music'   #getID(yt, user_username) #should relay back from getID function
    
)
'''

res = req.execute()
#res1 = req1.execute()
#chart = pd.DataFrame(res)
print(res)

print(json.dumps(res, indent=0))
#chart1 = pd.DataFrame(res1)
#print(chart1)

#pandas not supported because output is in JSON format

#npr id: UC4eYXhJI4-7wSWc8UNRwD4A

#getting the id of a channel given the username:
user_username = input()

def getID(yt, forUsername):
    req = yt.channels().list(
    part = 'id, statistics, snippet',
    forUsername = user_username   #sample username from schafer
)
    
    res = req.execute()
    
    for item in res['items']:
        new_id = item['id']
        
    return new_id

#outside function
new_channelID = getID(yt, user_username)
print(new_channelID)

#new function
def getVideosId(youtube, channelId):
    '''
    Get list of all videos ids in youtube channle
    
    Args:
        youtube (servibe object):
        channelId (string): the channel id 
        
    Return:
        a list of videos ids
    '''
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

print('Enter Username to show all links to Videos and channel info: ' )
user_username = input()
list_vids = getVideosId(yt, getID(yt,user_username))

links = []

for ids in list_vids:
    newlink = 'https://www.youtube.com/watch?v=' + ids
    links.append(newlink)

chart = pd.DataFrame(links)
print(chart)
#list of all video id's

#new project idea.

#return all video's where user input username of channel

#https://www.youtube.com/watch?v=
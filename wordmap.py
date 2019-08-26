#!/usr/bin/env python

import requests
import os
import json
from wordcloud import WordCloud

requests.packages.urllib3.disable_warnings()


user_id = 6
myList = []

def loadEvents(numPages): 
    for i in range(1, numPages):
      print(i)
      url = "https://gitlab.%s.com/api/v4/users/%s/events?per_page=100&page=%s" % (os.getenv('COMPANY'), user_id, i)
      auth = os.getenv('AUTH')
      payload = ""
      querystring = {}
      headers = {
              'Authorization': "Basic %s" % auth,
              'cache-control': 'no-cache'
              }
      response = requests.request("GET", url, data=payload, headers=headers, verify=False)
      responseJson = json.loads(response.text)
      for result in responseJson:
        try:
          myList.append(result['push_data']['commit_title'] + ' ')
        except: 
          pass



loadEvents(10)

myCloud = ''.join(myList)
wordcloud = WordCloud(max_words=500, random_state=1, width=800,height=800).generate(myCloud)
wordcloud.to_file('holden_wordcloud.png')

# akhbaar padhke sunao

# import requests
# import json
# def speak(str):
#     from win32com.client import Dispatch
#     speak=Dispatch("SAPI.SpVoice")
#     speak.Speak(str)
# if __name__=='__main__':
#     r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=02b1c4b432e44682b24605172e133564")
#     data=r.text
#     parsed=json.loads(data)
#     news_list=parsed["articles"]
#     print("press ctrl+c to stop the app...")
#     for news_dict in news_list:
#         speak(news_dict["description"])

import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__=='__main__':
    speak("News for today...Let's begin")
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=02b1c4b432e44682b24605172e133564"
    news=requests.get(url).text
    news_dict=json.loads(news)
    arts=news_dict['articles']
    for i,article in enumerate(arts):
        speak(article['title'])
        print(article['title'])
        if i==len(arts)-1:break
        speak("Moving on to the next news...Listen carefully")
    speak("Thanks for listening")
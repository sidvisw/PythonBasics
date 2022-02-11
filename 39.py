#healthy programmer
# 9am-5pm
# water-water.mp3 (3.5 lit)-Drank-log-every 40 min
# eyes-eyes.mp3-every 30 min EyDone-log
# physical activity-physical.mp3 every-45 min ExDone-log

# Rules
# Pygame module to play audio


# from pygame import mixer
# import time
# def getdate():
#     import datetime
#     return datetime.datetime.now()
# water_done=1
# eye_done=1
# physical_done=1
# def Write(f,s):
#     f.write("[")
#     f.write(str(getdate()))
#     f.write("]")
#     f.write(" ")
#     f.write(s)
#     f.write("\n")
# print('to exit from the application press ctrl+c')
# while(1):
#     time.sleep(30*60)
#     eye_done=0
#     if(water_done==1 and physical_done==1):
#         print("eye exercise time...")
#         mixer.init()
#         mixer.music.load("eye.mp3")
#         mixer.music.set_volume(0.7)
#         mixer.music.play()
#         str1=input("type eydone when you finish : ")
#         if(str1=="eydone"):
#             eye_done=1
#             mixer.music.stop()
#             f=open("file.txt","a")
#             Write(f,"eye exercise done")
#             f.close()
#     time.sleep(15*60)
#     physical_done=0
#     if(water_done==1 and eye_done==1):
#         print("physical exercise time...")
#         mixer.init()
#         mixer.music.load("physical.mp3")
#         mixer.music.set_volume(0.7)
#         mixer.music.play()
#         str1=input("type exdone when you finish : ")
#         if(str1=="exdone"):
#             physical_done=1
#             mixer.music.stop()
#             f=open("file.txt","a")
#             Write(f,"physical exercise done")
#             f.close()
#     time.sleep(15*60)
#     water_done=0
#     if(eye_done==1 and physical_done==1):
#         print("drink 2 glass of water...")
#         mixer.init()
#         mixer.music.load("water.mp3")
#         mixer.music.set_volume(0.7)
#         mixer.music.play()
#         str1=input("type drank when you finish : ")
#         if(str1=="drank"):
#             water_done=1
#             mixer.music.stop()
#             f=open("file.txt","a")
#             Write(f,"drank water")
#             f.close()

from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("file.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__=='__main__':
    # musiconloop("water.mp3","stop")
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    watersecs=40*60
    exsecs=45*60
    eyesecs=30*60
    while True:
        if time()-init_water>watersecs:
            print("water drinking time. enter 'drank' to stop the alarm.")
            musiconloop('water.mp3','drank')
            init_water=time()
            log_now("drank water at")
        if time()-init_eyes>eyesecs:
            print("eye exercise time. enter 'eydone' to stop the alarm.")
            musiconloop('eye.mp3','eydone')
            init_eyes=time()
            log_now("eyes relaxed at")
        if time()-init_exercise>exsecs:
            print("physical activity time. enter 'exdone' to stop the alarm.")
            musiconloop('physical.mp3','exdone')
            init_exercise=time()
            log_now("physical activity done at")
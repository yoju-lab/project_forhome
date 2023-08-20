import datetime
import time
import pygame

pygame.init()

# 입력 받은 시간에 따라 음악이 재생되도록 설정합니다.
def play_music(hour, minute):
    # 현재 시간을 가져옵니다.
    now_time = datetime.datetime.now()
    # 재생되어야 하는 시간을 계산합니다.
    next_time = datetime.datetime(now_time.year, now_time.month, now_time.day, hour, minute)

    # 다음 날로의 시간을 계산합니다.
    if next_time <= now_time:
        # next_time += datetime.timedelta(days=0)   # when testing
        next_time += datetime.timedelta(days=1)     # when operating

    # 다음 시간까지 대기합니다.
    time.sleep((next_time - now_time).seconds)

    filepath = 'datasets/tvari-tokyo-cafe-159065.mp3'
    # 음악이 일정 시간동안 재생됩니다.
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    # 음악 파일의 길이(sec)를 계산합니다.
    length = pygame.mixer.Sound(filepath).get_length()
    # 길이 만큼 sleep 합니다.
    pygame.time.wait(int(length * 1000))
    
    pygame.mixer.music.stop()

    return "음악이 재생되었습니다."

if __name__ == '__main__':
    #입력받은 시, 분에 음악이 재생되도록 설정합니다.
    hour, minute = map(int, input("시 분을 입력하세요(ex. 12 30): ").split())

    print(play_music(hour, minute))

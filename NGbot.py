# import vk_api
# from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
# from vk_api import VkUpload 
from pprint import *
import random
import dataTask
import time

TIME_SLEEP = 300 # 5min / 12task/h
ITERATIONS = 120
vk_session = vk_api.VkApi(token = 'b7a5b95ab2d5170a0b6dd7cc9a5918d007e45d58ad15b78db2e42f46b26d426664ecd6d61839b500059f9')
longpoll = VkBotLongPoll(vk_session,group_id=187643301)
vk = vk_session.get_api()

dataReg = vk.groups.getLongPollServer(group_id=187643301 )

users = vk.messages.getConversationMembers(
                                        peer_id=2000000005, #2000000002 квартира  2000000003 тест 
                                        group_id=187643301
                                            )

usersID = []
usersFirstName = []

task = dataTask.tasks
alckohol = dataTask.alckohol
countUser = users['count']

for user in users['profiles']:

    usersID.append(user['id'])
    usersFirstName.append(user['first_name'])

# pprint(usersID)
# pprint(usersFirstName)


def selectRandomUser(usersIdList: list, usersFirstName: list):
    numberIndex = random.randint(0,len(usersIdList)-1)
    return(usersIdList[numberIndex], usersFirstName[numberIndex])

def selectRandomTask(taskList: list, alckoholList: list):
    numberIndexTask = random.randint(0,len(taskList)-1)
    task = taskList[numberIndexTask]
    
    if task == 'Пей':
        numberIndexAlckohol = random.randint(0,len(alckoholList)-1)
        alckohol = alckoholList[numberIndexAlckohol]

        return task + alckohol
    return task 

for event in longpoll.listen():
    # pprint.pp(event)
    print('[OK]')
    print(event)
    pprint(event.object)

    if event.type == VkBotEventType.MESSAGE_NEW :
        # print(event.object.text)

        if event.object.text == '[club187643301|@room_84] time2':
            TIME_SLEEP = 120
        elif event.object.text == '[club187643301|@room_84] time3':
            TIME_SLEEP = 180
        elif event.object.text == '[club187643301|@room_84] time4':
            TIME_SLEEP = 240
        elif event.object.text == '[club187643301|@room_84] time6':
            TIME_SLEEP = 360
        elif event.object.text == '[club187643301|@room_84] time10':
            TIME_SLEEP = 600

    messag = event.object.text.split('|')


    # print(messag)
    if event.from_chat and messag[0] == '[club187643301':

        # vk.messages.send(
        #             key = dataReg['key'],
        #             server = dataReg['server'],
        #             ts=dataReg['ts'],
        #             random_id = get_random_id(),
        #             message=f'@all Скорон НГ вы готовы?',
        #             chat_id = event.chat_id
        #         )

        for _ in range(ITERATIONS):
            
            sendForUserID = selectRandomUser(usersID, usersFirstName)
            sendForUserFirstName = sendForUserID[1]
            sendForUserID = sendForUserID[0]
            # sendForUserFirstName = selectRandomUser(usersID, usersFirstName)[1]
            sendTask = selectRandomTask(dataTask.tasks, dataTask.alckohol)
            sendSpeedReed = selectRandomTask(dataTask.speedRead, dataTask.alckohol)[0]
            
            sendForUserID2 = selectRandomUser(usersID, usersFirstName)
            sendForUserFirstName2 = sendForUserID2[1]
            sendForUserID2 = sendForUserID2[0]
            # sendForUserFirstName2 = selectRandomUser(usersID, usersFirstName)[1]
            
            # if sendForUserID == 105431859 or sendForUserID2 == 105431859:
            #     numberIndexAlckohol = random.randint(0,len(alckoholList)-1)
            #     alckohol = alckoholList[numberIndexAlckohol]
                
            #     vk.messages.send(
            #         key = dataReg['key'],
            #         server = dataReg['server'],
            #         ts=dataReg['ts'],
            #         random_id = get_random_id(),
            #         message=f'[id{sendForUserID}|@{sendForUserFirstName}] {sendTask} ',
            #         chat_id = event.chat_id
            #     )

            #     time.sleep(TIME_SLEEP)
            #     continue

            # Together    
            if sendTask == 'Целуется с' or sendTask == 'Уходит в выручай комнату с' or sendTask == 'Идет на хуй' or sendTask == 'Мечтает о' or sendTask == 'Cнимает элемент одежды c':
                vk.messages.send(
                    key = dataReg['key'],
                    server = dataReg['server'],
                    ts=dataReg['ts'],
                    random_id = get_random_id(),
                    message=f'[id{sendForUserID}|@{sendForUserFirstName}] {sendTask} [id{sendForUserID2}|@{sendForUserFirstName2}]',
                    chat_id = event.chat_id
                )
            
            # ALL     
            elif sendTask == 'Не отвечают на вопросы' or sendTask == 'ЗОЛОТЫЕ СЛОВА' or sendTask == 'Играют в пьяную 3':
                
                # ALL no time
                if sendTask == 'ЗОЛОТЫЕ СЛОВА' or sendTask == 'Играют в пьяную 3':
                    vk.messages.send(
                        key = dataReg['key'],
                        server = dataReg['server'],
                        ts=dataReg['ts'],
                        random_id = get_random_id(),
                        message=f'@all {sendTask} ',
                        chat_id = event.chat_id
                    )

                    time.sleep(TIME_SLEEP)
                    continue

                randomMin = random.randint(2,5)

                vk.messages.send(
                    key = dataReg['key'],
                    server = dataReg['server'],
                    ts=dataReg['ts'],
                    random_id = get_random_id(),
                    message=f'@all {sendTask} [id{sendForUserID}|@{sendForUserFirstName}] {randomMin}мин',
                    chat_id = event.chat_id
                )

                time.sleep(randomMin*60)
                
                vk.messages.send(
                    key = dataReg['key'],
                    server = dataReg['server'],
                    ts=dataReg['ts'],
                    random_id = get_random_id(),
                    message=f'@all Время вышло',
                    chat_id = event.chat_id
                )

            # One
            elif sendTask == 'Молчит' or sendTask == 'Сидит под столом' or sendTask == 'Рассказывает историю' or sendTask == 'Говорит скороговорку':
                
                # One reed no time
                if sendTask == 'Говорит скороговорку':
                    vk.messages.send(
                        key = dataReg['key'],
                        server = dataReg['server'],
                        ts=dataReg['ts'],
                        random_id = get_random_id(),
                        message=f'[id{sendForUserID}|@{sendForUserFirstName}] {sendTask} {sendSpeedReed}',
                        chat_id = event.chat_id
                    )

                    time.sleep(TIME_SLEEP)
                    continue
                
                randomMin = random.randint(1,3)

                vk.messages.send(
                    key = dataReg['key'],
                    server = dataReg['server'],
                    ts=dataReg['ts'],
                    random_id = get_random_id(),
                    message=f'[id{sendForUserID}|@{sendForUserFirstName}] {sendTask} {randomMin}мин',
                    chat_id = event.chat_id
                )
                time.sleep(randomMin*60)
                
                vk.messages.send(
                    key = dataReg['key'],
                    server = dataReg['server'],
                    ts=dataReg['ts'],
                    random_id = get_random_id(),
                    message=f'[id{sendForUserID}|@{sendForUserFirstName}] Время вышло',
                    chat_id = event.chat_id
                )

            # Drink
            else:
                vk.messages.send(
                    key = dataReg['key'],
                    server = dataReg['server'],
                    ts=dataReg['ts'],
                    random_id = get_random_id(),
                    message=f'[id{sendForUserID}|@{sendForUserFirstName}] {sendTask} ',
                    chat_id = event.chat_id
                )

            time.sleep(TIME_SLEEP)
import pytchat
from time import sleep
import pyautogui
import datetime

streamID = ''
chat = pytchat.create(streamID)
soundQ = []
hotKeyword = []
hotKeyFind = {}
punctuation = '@#$%^&*()_+=-`;:"?/>.<,`~|'
recommend = []
mutedPeople = []

while chat.is_alive():
    for chat_message in chat.get().items:
        print(f"{chat_message.author.name}: {chat_message.message}")
        textWords = chat_message.message.lower().strip(punctuation).split()
        i = 0
        for thing in textWords:
            textWords[i] = thing.strip(',')
            i += 1
        print(textWords)
        #update MUTES
        with open("MUTED_PEOPLE_FOR_SOUND_EFFECTS.txt", "r") as file:
            unsplitData = file.read()
            mutedPeople = unsplitData.split()
            print(f'{unsplitData} US')
            print(mutedPeople)
        for name in mutedPeople:
            if chat_message.author.name == name:
                print('cant speak')
            else:
                print('can speak')
                #end mute update
                if textWords[0] == '!':
                    for word in textWords:
                        if word in hotKeyword:
                            soundQ.append(word)
        
                    while len(textWords) > 0:
                            textWords.pop(0)
        
                    print(soundQ)
                        #if you want you can try and fix the code below, but i will most likely fix it myself
                        #combine split words
                        #if len(soundQ) > 1:
                        #    if soundQ[0] and soundQ[1] == 'womp':
                        #        soundQ[0] = soundQ[0] + ' ' + soundQ[1]
                        #       soundQ.pop(1)
                        #tri noise
                    while len(soundQ) > 0:
                        print('running sound')
                        print(soundQ[0])
                        print(hotKeyFind[soundQ[0]])
                        keyToPress = hotKeyFind[soundQ[0]]
                        pyautogui.press(keyToPress)
                        sleep(1)
                        soundQ.pop(0)
                        print(soundQ)
                elif textWords[0] == 'recommend':
                    print(f'{chat_message.author.name} wants to {chat_message.message}')
                    r = chat_message.author.name, ' wants to ', chat_message.message
                    recommend.append(r)
                    day = datetime.date.today()
                    with open("recommendations.txt", "a") as file:
                        file.write(f'{r}, When?: {day}, {chat_message.author.name}')
                        file.write('      ')
                    print(recommend)

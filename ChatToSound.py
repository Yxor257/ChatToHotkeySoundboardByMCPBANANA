import pytchat
from time import sleep
import pyautogui
import datetime

streamID = ''
chat = pytchat.create(streamID)
soundQ = []
#DO YOU HAVE A MAIL SOUND IF SO SET THIS TO TRUE AND SCROLL TO THE BOTTOM TO CHANGE THE INPUT KEY
hasRecommendationSound = False
#single words only
hotKeyword = []
# place multi long words as a sentence (DOES NOT FUNCTION)
#multi_Long_Keywords = ['example statement', 'example split']
# you can put all the keyword stuff in here
hotKeyFind = {}
punctuation = '@#$%^&*()_+=-`;:"?/>.<,`~|'
#DO NOT EDIT RECOMMEND OR MUTED PEOPLE LIST VAR'S
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
        for name in mutedPeople:
            if chat_message.author.name == name:
                print('Muted')
            else:
                print('can speak')
                #end mute update
                print('running')
                if textWords[0] == '!':
                    for word in textWords:
                        if word in hotKeyword:
                            soundQ.append(word)

                    while len(textWords) > 0:
                        textWords.pop(0)

                    print(soundQ)
                    #wordJoiner = 0
                    #if len(soundQ) > 1:
                    #    for wordA in soundQ:
                    #        multWord = multi_Long_Keywords[wordJoiner]
                    #        wordB = soundQ[wordJoiner + 1]
                    #        if wordA in multWord[wordJoiner]:
                    #            if wordB in multWord[wordJoiner+1]:
                    #                combined_word = wordA, ' ', wordB
                    #                soundQ.pop(wordJoiner+1)
                    #                soundQ[wordJoiner] = combined_word
                    #        wordJoiner += 1
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
                        file.write(f'{r}, When?: {day}')
                        file.write('        ')
                        print(recommend)
                        if hasRecommendationSound:
                            pyautogui.press('CHANGE')

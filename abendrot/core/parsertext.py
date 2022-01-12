


def parse(input_text):
    command = input_text.lower()
    object1 = None

    # the .split() function splits the input_text string variable into a python list of individual words
    words = input_text.split()

    if len(words) > 0:        
        remaining_words_index = 0
        examineActions = ('look', 'inspect', 'check', 'examine', 'study')
        moveActions = ('move', 'walk', 'travel', 'go')
        talkActions = ('talk', 'chat')

        foundExaminewords = False
        if words[0] in examineActions:
            remaining_words_index = 1
            foundExaminewords = True
        if words[0] == "look" and words[1] == "at":
            remaining_words_index = 2
            foundExaminewords = True
            
        if foundExaminewords:
            if len(words) > remaining_words_index:
                remaining_words = ""
                for i in range(remaining_words_index, len(words)):
                    remaining_words += words[i]
                    if i < len(words)-1:
                        remaining_words += " "
                command = "examine"
                object1 = remaining_words.lower()
        
        foundMovewords = False
        if words[0] in moveActions:
            remaining_words_index = 1
            foundMovewords = True
        if (words[0] == 'travel' or words[0] == 'go' or words[0] == 'move' or words[0] == 'walk') and words[1] == 'to':
            remaining_words_index = 2
            foundMovewords = True

        if foundMovewords:
            if len(words) > remaining_words_index:
                remaining_words = ""
                for i in range(remaining_words_index, len(words)):
                    remaining_words += words[i]
                    if i < len(words) - 1:
                        remaining_words += " "
                    command = 'move'
                    object1 = remaining_words.lower()

        foundChatwords = False
        if words[0] in talkActions:
            remaining_words_index = 1
            foundChatwords = True
        if words[0] == 'talk' or words[0] == 'chat' and words[1] == 'with':
            remaining_words_index = 2
            foundChatwords = True
        
        if foundChatwords:
            if len(words) > remaining_words_index:
                remaining_words = ""
                for i in range(remaining_words_index, len(words)):
                    remaining_words += words[i]
                    if i < len(words)-1:
                        remaining_words += " "
                command = "talk"
                object1 = remaining_words.lower()

        found_take_words = False
        if (words[0] == "take") and len(words) > 1:
            found_take_words = True
            remaining_words_index = 1

        if (words[0] == "pick") and (words[1] == "up") and len(words) > 2:
            found_take_words = True
            remaining_words_index = 1

        if found_take_words:
            remaining_words = ""
            for i in range(remaining_words_index, len(words)):
                remaining_words += words[i]
                if i < len(words)-1:
                    remaining_words += " "
            command = "take"
            object1 = remaining_words.lower()
        
    return command, object1

with open("story.txt","r") as f:
    story = f.read()
    print(story)
words =[]
start_of_word = -1

target_start= "<"
target_end=">"


for i, char in enumerate(story):
    # print(i)
    # print(char)
    if char==target_start:
        start_of_word=i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word:i+1]
        print(start_of_word)
        print(i+1)
        print(word)
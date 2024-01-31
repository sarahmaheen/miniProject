with open("story.txt","r") as f:
    story = f.read()
    print(story)
words =set()
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
        # slicing the words from the story!!!!!
        # print(start_of_word)
        # print(i+1)
        # print(word)
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for" + word + ":")
    answers[word] = answer
    print(word)
    print(answers[word])

for word in words:
    story = story.replace(word, answers[word])

# print(words)
# print(answers)
print(story)
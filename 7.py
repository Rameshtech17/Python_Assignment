"""
7. text = "I am a programmer! I often write code to solve day-to-day problems"
words = ["program", "clean", "gram", "ten", "code", "right"]

Print the words that are present in the "text" sentence given. (Write a code that works for any given inputs text and words)

Expected O/P: ["program", "gram", "ten", "text"]

"""
final = []
text = "I am a programmer! I often write code to solve day-to-day problems"
words = ["program", "clean", "gram", "ten", "code", "right"]

for k in range(0, words.__len__()):
    if words[k] in text:
        final.append(words[k])

print(final)
"""
Output:


program
gram
ten
code

"""
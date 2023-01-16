# word = input().lower()
#
# print(word.count("sun") + word.count("sand") + word.count("water") + word.count("fish"))
#



# user_input = input().lower()
# counter = 0
# beach_words = ["sand", "water", "fish", "sun"]
# for n in beach_words:
#     counter += user_input.count(n)
# print(counter)


text = input().lower()

my_list = ["sand", "water", "fish", "sun"]
counter = 0

for item in my_list:
    if item in text:
        word_count_txt = text.count(item)
        counter += word_count_txt

print(counter)
string = "big black bug bit a big black dog on his big black nose";
string = string.lower();
words = string.split(" ");
print("Duplicate words in a given string : ");
for i in range(0, len(words)):
    count = 1;
    for j in range(i + 1, len(words)):
        if (words[i] == (words[j])):
            count = count + 1;
            words[j] = "0";
    if (count > 1 and words[i] != "0"):
        print(words[i]);

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))

def check_space(string):
    count = 0
    for i in range(0, len(string)):
        if string[i] == " ":
            count += 1
    return count
string = "Welcome to geeksforgeeks"
print("number of spaces ", check_space(string))
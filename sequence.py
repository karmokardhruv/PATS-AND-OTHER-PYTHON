# Checks for the largest common prefix
def lcp(s, t):
    n = min(len(s), len(t));
    for i in range(0, n):
        if (s[i] != t[i]):
            return s[0:i];
    else:
        return s[0:n];
str = "balls nuts orbs spheres nuts";
lrs = "";
n = len(str);
for i in range(0, n):
    for j in range(i + 1, n):
        # Checks for the largest common factors in every substring
        x = lcp(str[i:n], str[j:n]);
        # If the current prefix is greater than previous one
        # then it takes the current one as longest repeating sequence
        if (len(x) > len(lrs)):
            lrs = x;
print("Longest repeating sequence: " + lrs);

my_lst = ['I','Love','Python','very','much','I','Love','Python','good','nice','I','Love','Python','I','Love','Python']

min_Seq_length = 2

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

all_sequences = []
for seq_length in range(min_Seq_length, + 1):
    all_sequences += [val for val in find_ngrams(my_lst, seq_length)]

print(Counter(all_sequences).most_common(1)[0])
def word_order():
    n = int(input("Kitne words hain? "))

    words = []
    counts = {}

    for _ in range(n):
        word = input().strip()
        if word not in counts:
            words.append(word)      
            counts[word] = 1
        else:
            counts[word] += 1

    print(len(words))               
    for w in words:
        print(w, counts[w])         

if __name__ == '__main__':
    word_order()

def word_order_from_file(filename):
    words = []
    counts = {}

    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())  

        for line in lines[1:n+1]:  
            word = line.strip()
            if word not in counts:
                words.append(word)
                counts[word] = 1
            else:
                counts[word] += 1

    
    print(len(words))  
    for w in words:
        print(w, counts[w])  


if __name__ == '__main__':
    filename = input("Enter the filename (with .txt): ")
    word_order_from_file(filename)

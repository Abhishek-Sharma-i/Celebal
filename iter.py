from itertools import combinations

def probability_of_a():
    n = int(input())                     
    letters = list(input().strip())      
    k = int(input())                     

    indices = list(range(n))
    comb = list(combinations(indices, k))

    favorable = 0
    for c in comb:
        if 'a' in [letters[i] for i in c]:
            favorable += 1

    probability = favorable / len(comb)
    print(f"{probability:.4f}")

# Run the function
probability_of_a()

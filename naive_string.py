Given: A text string text of length n. A pattern string pattern of length m. Find all starting indices i in the text such that the substring text[i:i+m] is exactly equal to the pattern pattern, using the Naive String Matching Algorithm approach. 
Constraints: l 0 ≤ m ≤ n l Characters in text and pattern can be any valid characters (e.g., a–z, A–Z, digits, etc.)




# Function to find all occurrences of pattern in text
def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    indices = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            indices.append(i)
    return indices

# ------------------- Main -------------------
text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

indices = naive_string_match(text, pattern)

if indices:
    print(f"Pattern found at indices: {indices}")
else:
    print("Pattern not found")

OUTPUT:
Enter the text: ABCDABCDABCD
Enter the pattern: ABC
Pattern found at indices: [0, 4, 8]


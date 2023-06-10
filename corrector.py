import nltk
from nltk.corpus import words

# Load English dictionary words
nltk.download('words')
english_words = set(words.words())

# Function to calculate Levenshtein distance
def levenshtein_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[m][n]

# Auto-correct function
def autocorrect(word):
    suggestions = []
    min_distance = float('inf')

    for dict_word in english_words:
        distance = levenshtein_distance(word, dict_word)
        if distance < min_distance:
            suggestions = [dict_word]
            min_distance = distance
        elif distance == min_distance:
            suggestions.append(dict_word)

    return suggestions

# Test the auto-correct function
input_word = "speling"  # Word with a spelling mistake
suggested_words = autocorrect(input_word)

print("Input word:", input_word)
print("Suggested words:", suggested_words)

def is_valid_change(word1, word2):
   """Check if word2 differs from word1 by only one letter."""
   if len(word1) != len(word2):
       return False
   return sum(1 for a, b in zip(word1, word2) if a != b) == 1

start_word = "cat"
goal_word = "dog"
current_word = start_word

print(f"Word Ladder Game! Transform '{start_word}' to '{goal_word}' one letter at a time.")

while current_word != goal_word:
   new_word = input(f"Enter a word that changes one letter in '{current_word}': ").lower()

   if not is_valid_change(current_word, new_word):
       print("Invalid move! Your word must change exactly one letter.")
   else:
       current_word = new_word

print(f"Congratulations! You turned '{start_word}' into '{goal_word}'! ????")
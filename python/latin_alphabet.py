"""Generate map 'index -> latin letter'. Convenient for Leetcode puzzles."""
import string

cipher = {}
for i, letter in enumerate(string.ascii_uppercase):
    cipher[str(i + 1)] = letter

print(cipher)

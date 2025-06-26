# This script prints a simple ASCII art kitten using five lines,
# followed by five additional lines with a friendly message.

kitten_art = [
    " /\\_/\\",
    "( o.o )",
    " > ^ <",
    "  /|\\",
    " (___)"
]

message_lines = [
    "A tiny kitten appears!",
    "Isn't it cute?",
    "Take it for a test run",
    "on your local machine",
    "and enjoy!"
]

for line in kitten_art + message_lines:
    print(line)

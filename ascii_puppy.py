# This script prints a simple ASCII art puppy using five lines,
# followed by five additional lines with a friendly message.

puppy_art = [
    " /^ ^\\",
    "/ 0 0 \\",
    "V\\ Y /V",
    " / - \\",
    "|_| |_|"
]

message_lines = [
    "A playful puppy wags its tail!",
    "Ready for some fetch?",
    "Run the script on your laptop",
    "and watch the puppy play!",
    "Woof woof!"
]

for line in puppy_art + message_lines:
    print(line)

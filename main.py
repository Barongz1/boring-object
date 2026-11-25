"""The Most Boring Object, Reviewed in One Line — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The review: the doorstop does nothing all day, and still does it better than me.
TEXT = "One star. The doorstop does nothing all day, and somehow it still does it better than me."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()

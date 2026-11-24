import os

TEXT = "One percent left. Truth is, I have been at one percent for twenty minutes. I just wanted the attention."

def main():
    assert 1 <= len(TEXT) <= 199 and TEXT.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()

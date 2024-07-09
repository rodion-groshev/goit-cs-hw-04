from threading import Thread
from time import time

files = ["first.txt", "second.txt", "third.txt", "fourth.txt"]
matches = []


def find_words(file, word):
    start_time = time()
    try:
        with open(file, "r") as f:
            text = f.readline().split()
            for i in range(len(text)):
                if text[i].lower() == word:
                    matches.append((text[i], i, file))
    except FileNotFoundError as e:
        print(e)

    end_time = time()
    print(f"Execute time for file {file}: {end_time - start_time}")


if __name__ == '__main__':
    threads = []
    for name in files:
        thread = Thread(target=find_words, args=(name, "he"))
        thread.start()
        threads.append(thread)

    [el.join() for el in threads]
    print(matches)

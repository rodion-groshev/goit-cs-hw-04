from multiprocessing import Queue, Process
from time import time

files = ["first.txt", "second.txt", "third.txt", "fourth.txt"]
q = Queue()


def find_words(file, word, queue):
    start_time = time()
    try:
        with open(file, "r") as f:
            text = f.readline().split()
            for i in range(len(text)):
                if text[i].lower() == word:
                    queue.put((text[i], i, file))
    except FileNotFoundError as e:
        print(e)

    end_time = time()
    print(f"Execute time for file {file}: {end_time - start_time}")


if __name__ == '__main__':
    processes = []
    for name in files:
        process = Process(target=find_words, args=(name, "he", q))
        process.start()
        processes.append(process)

    [el.join() for el in processes]

    while not q.empty():
        print(q.get())

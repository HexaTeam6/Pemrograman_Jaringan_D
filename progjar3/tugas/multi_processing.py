
from multiprocessing import Lock, Process, Queue, current_process
import time
import queue


def do_job(tasks_to_accomplish, tasks_that_are_done):
    while True:
        try:
            task = tasks_to_accomplish.get_nowait()
        except queue.Empty:

            break
        else:
            print(task)
            tasks_that_are_done.put(task + ' diselesaikan oleh proses ' + current_process().name)
            time.sleep(.5)
    return True


def main():
    number_of_task = 10
    number_of_processes = 4
    tasks_to_accomplish = Queue()
    tasks_that_are_done = Queue()
    processes = []

    for i in range(number_of_task):
        tasks_to_accomplish.put("Task no " + str(i))

    # buat proses
    for w in range(number_of_processes):
        p = Process(target=do_job, args=(tasks_to_accomplish, tasks_that_are_done))
        processes.append(p)
        p.start()

    #jalankan proses
    for p in processes:
        p.join()

    # tampilkan hasilnya
    while not tasks_that_are_done.empty():
        print(tasks_that_are_done.get())

    return True


if __name__ == '__main__':
    main()
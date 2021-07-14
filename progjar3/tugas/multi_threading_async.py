import time
import socket
import logging
import datetime
import threading
import concurrent.futures
from multiprocessing import Process, Pool
import os
import sys

# target IP kirim_sync
TARGET_IP = "192.168.122.255"  # Bcast = Broadcast Address
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def kirim_multi_thread_async(daftar=None):
    if (daftar is None):
        return False
    f = open(daftar, "rb")
    l = f.read(1024)
    while (l):
        if (sock.sendto(l, (TARGET_IP, TARGET_PORT))):
            l = f.read(1024)
    f.close()


def multi_thread_async():
    texec = dict()
    daftar = ['testing1.png', 'testing2.jpeg']
    status_task = dict()
    task = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    catat_awal = datetime.datetime.now()
    for k in range(len(daftar)):
        print(f"mendownload {daftar[k]}")
        waktu = time.time()
        texec[k] = task.submit(kirim_multi_thread_async, daftar[k])
    for k in range(len(daftar)):
        status_task[k] = texec[k].result()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("hasil task yang dijalankan")
    print(status_task)

multi_thread_async()
#!/usr/bin/env python

from multiprocessing import Pool
import os
import time
import random
import subprocess

videolist = [

]

def download_task(name, command):
    print('Run task %s (%s)...' % (name, os.getpid()))
    print('command is %s' %(command))
    start = time.time()
    with subprocess.Popen(command) as process:
        print(r"youtube-dl return code :", process.returncode)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    task_number = len(videolist)
    p = Pool(4)
    for i in range(task_number):
        command = " ".join([
            r"youtube-dl",
            r"--format", r"best",
            # r"--get-filename",
            # r"--output", r'"%(playlist)s-%(title)s.%(ext)s"',
            videolist[i],
        ])

        p.apply_async(download_task, args=(i, command))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

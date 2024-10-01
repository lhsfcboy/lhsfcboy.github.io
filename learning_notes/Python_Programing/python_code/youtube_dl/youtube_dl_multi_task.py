# -*- coding: utf-8 -*-
#!/usr/bin/env python 

# TODO 使得URL串中的#注释部分能够自动删除
from multiprocessing import Pool
import os, time, sys, subprocess

"""
"""



url_list = """
PLP1Ynr8cs97uUwxOJ4VD_Z3-NwzElPBdN

PLP1Ynr8cs97tD5OmChMl9LYTV-KOnWFD3
PLP1Ynr8cs97uJakFfEPJUduE8pRapPGjb
PLP1Ynr8cs97tPCMS0jOEYFNJoz7CelIJ5
PLP1Ynr8cs97uf0bKABAZ918BJkQAi8Wap
PLP1Ynr8cs97sDn2fNAePRVY_keIq0ACs0
PLP1Ynr8cs97sCOdgQ91C6HR0hPNU8w2xR
PLP1Ynr8cs97tXstIH1RIKwB0RpGJN3IWV
PLP1Ynr8cs97sTy5JH2Bpd1-gyOdu1_24Q
PLP1Ynr8cs97uudkoeZ4hzjyfuleKK61UL
PLP1Ynr8cs97vgRUr2boGNe1ndRVuzGyG4
PLP1Ynr8cs97sYNRap1CE3APvwiAO28Ezc
PLP1Ynr8cs97txLGE3pUznO8ziGAyh3F30
PLP1Ynr8cs97v-WvYIYEfHTprbSh7OY8jg
PLP1Ynr8cs97svoTyg4iLr6bSiOWpTNwHH
PLP1Ynr8cs97vtneWy-QZ3R1kznRv2BR4B
PLP1Ynr8cs97tBbH9zQ9Qyw0EF2q51SPzh
PLP1Ynr8cs97tsD5JomGc34i44MPgEefsX
PLP1Ynr8cs97sLC7PtYzgtuHIifEajWUmh
PLP1Ynr8cs97tgRZqrgiys-3WfQJT4KUYG
PLP1Ynr8cs97uxfVBlbwfV2ZzNhU5gIQMP
PLP1Ynr8cs97t5dcAbH1ktu4hQg7n5Zcjm
PLP1Ynr8cs97sPAm9F3ZWN_DtJPoPtTit5
PLP1Ynr8cs97uF01DU-511rFxLN1ZpM31z
PLP1Ynr8cs97umc5flZIGDsnchOgXUp_Uc
PLP1Ynr8cs97tZMTIivMdpQ0TB-hAvdYFa
PLP1Ynr8cs97tXU2StDZMqmnrKWROoruwU
PLP1Ynr8cs97tpjKt2XAtzd36J8NGL6-Xd
PLP1Ynr8cs97vl4zw26qshI8xlOP70sgKe
PLP1Ynr8cs97tpW1VyWrVrEzdEJ5vTrpar
PLP1Ynr8cs97tqCTJ4b-L-M_HrxAOy2ojk
PLP1Ynr8cs97vU-Im8sWDk-s_Z9jOT8Eg1
PLP1Ynr8cs97soUmGIZ6NnpEVQGIGr82qS
"""

video_list = [item for item in url_list.splitlines() if item]



def download_task(name, command):
    print('Run task %s (%s)...' % (name, os.getpid()))
    print('command is %s' %(command))
    start = time.time()
    with subprocess.Popen(command) as process:
            print(r"youtube-dl return code :", process.returncode)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    os.chdir(os.path.dirname(sys.argv[0]))
    print("working on " + os.getcwd())
    print('Parent process %s.' % os.getpid())
    task_number = len(video_list)
    p = Pool(2)
    for i in range(task_number):
        command = " ".join([
            r"youtube-dl",
            r"--format", r"best",  
            r"--ignore-errors",
            #r"--no-progress",
            r"--newline",
            #r"--embed-subs",
            #r"--get-filename",  
            r"--output", r'"%(playlist)s-%(playlist_index)s-%(title)s.%(ext)s"',
            video_list[i],
        ])
        
        p.apply_async(download_task, args=(i,command))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

    input() 
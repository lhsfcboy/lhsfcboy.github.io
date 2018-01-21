import os
 
print( 'Process (%s) start...' % os.getpid())
pid = os.fork()

# 从这一刻起, 有两个进程在执行之下的代码
# 也就是说父进程执行一遍, 并print else分支
# 子进程也在同一时间执行, 并print if分支
if pid==0:
    print ('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print( 'I (%s) just created a child process (%s).' % (os.getpid(), pid))

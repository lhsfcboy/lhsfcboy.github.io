// 程序首先使用clock_getres()函数获取系统时钟的精度，并打印出来。
// 然后，它使用clock_gettime()函数获取当前时间（开始时间）。
// 程序使用usleep(100000)休眠100000微秒（即0.1秒）。
// 再次使用clock_gettime()获取当前时间（结束时间）。
// 最后，程序计算两次获取时间之间的差值，并打印出这个时间间隔。

// 这个程序展示了如何使用clock_gettime()函数进行高精度的时间测量。它使用CLOCK_REALTIME作为时钟源，这是系统的实时时钟。
// 需要注意的是，编译这个程序时需要链接实时库，因此编译命令中包含了-lrt选项。
// 这个程序可以用来测试系统时钟的精度和clock_gettime()函数的性能。在实际应用中，这种精确的时间测量可能用于性能分析、精确计时等场景。

#include <stdio.h>
#include <time.h>
#include <unistd.h>

//gcc -O2 -Wall -g  -lrt test_clock_gettime.c

int main(){
  struct timespec res,tp1,tp2;
  long sec,nsec;

  if(clock_getres(CLOCK_REALTIME,&res) < 0){
    perror("clock_getres");
    return 1;
  }
  printf("Time Precision:\t%ld.%09ld\n", (long)res.tv_sec, res.tv_nsec);

  if(clock_gettime(CLOCK_REALTIME,&tp1) < 0){
    perror("clock_gettime begin");
    return 2;
  }

  usleep(100000);

  if(clock_gettime(CLOCK_REALTIME,&tp2) < 0){
    perror("clock_gettime end");
    return 3;
  }
  sec = tp2.tv_sec - tp1.tv_sec;
  nsec = tp2.tv_nsec - tp1.tv_nsec;
  if(nsec < 0){
    sec--;
    nsec += 1000000000L;
  }
  printf("Time Span:\t%ld.%09ld\n",sec,nsec);
  return 0;
}

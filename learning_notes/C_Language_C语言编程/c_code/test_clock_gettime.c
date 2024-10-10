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

##include <cstdint>
#include <sys/time.h>
uint64_t nanotime(const struct timespec *ts)
{
   return (ts->tv_sec * kT_ns_in_s) + (ts->tv_nsec);
}

uint64_t    n=50000;
uint64_t    sum=0;
uint64_t    latency=0;

for (i = 0; i < n; i++) {
    clock_gettime(CLOCK_REALTIME, &start);
    clock_gettime(CLOCK_REALTIME, &end);
    sum += nanotime(&end) - nanotime(&start);
}

printf("Latency: %d ns\n", sum / n);


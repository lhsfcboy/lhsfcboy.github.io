#define __STDC_FORMAT_MACROS
#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <stdint.h>
#include <inttypes.h>

//gcc -O2 -Wall -g  -lrt test_clock_gettime.c


#define kT_ns_in_s  (uint64_t)1000000000
int main()
{
	uint64_t n = 500000;
	uint64_t sum = 0;
	uint64_t i = 0;


	uint64_t nanotime(const struct timespec *ts) {
		return (ts->tv_sec * kT_ns_in_s) + (ts->tv_nsec);
	}
	struct timespec start, end;
	for (i = 0; i < n; i++) {
		clock_gettime(CLOCK_REALTIME, &start);
		clock_gettime(CLOCK_REALTIME, &end);
		sum += nanotime(&end) - nanotime(&start);
	}

	printf("Latency: %" PRIu64 " ns\n", sum / n);
	//printf("Latency: %llu ns\n", sum / n);
	printf("--------------\n");
	return 0;
}

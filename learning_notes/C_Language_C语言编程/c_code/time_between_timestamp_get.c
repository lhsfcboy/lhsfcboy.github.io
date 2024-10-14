// 程序定义了一个常量 kT_ns_in_s，表示一秒钟包含的纳秒数（1,000,000,000）。
// 定义了一个内部函数 nanotime()，用于将 timespec 结构转换为纳秒数。
// 主循环执行 500,000 次，每次：

// 调用 clock_gettime() 获取开始时间
// 立即再次调用 clock_gettime() 获取结束时间
// 计算两次调用之间的时间差，并累加到 sum 中


// 最后，程序计算平均延迟（总时间差除以循环次数），并打印结果。

// 这个程序的主要目的是测量 clock_gettime() 函数本身的调用延迟。通过多次重复测量并取平均值，可以得到一个相对准确的延迟估计。
// 需要注意的几点：

// 使用 __STDC_FORMAT_MACROS 和 <inttypes.h> 来支持 PRIu64 宏，这用于正确打印 64 位整数。
// 程序使用 CLOCK_REALTIME 作为时钟源。在某些系统上，使用 CLOCK_MONOTONIC 可能会得到更精确的结果。
// 编译时需要链接实时库，因此编译命令中应包含 -lrt 选项。

// 要编译并运行这个程序，可以使用以下命令：
// gcc -O2 -Wall -g -lrt test_clock_gettime.c -o test_clock_gettime
// ./test_clock_gettime

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

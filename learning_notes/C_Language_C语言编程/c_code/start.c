// 生成一个柱状图
// 4       3       3       1       9       3       5       6       7       0
// *       *       *               *       *       *       *       *       
// *       *       *               *       *       *       *       *       
// *       *       *               *       *       *       *       *       
// *                               *               *       *       *       
//                                 *               *       *       *       
//                                 *                       *       *       
//                                 *                       *       *       
//                                 *                               *       
//                                 *

#include <stdio.h>
#define N 10

int main(void)
{
    int a[N] = {4, 3, 3, 1, 9, 3, 5, 6, 7, 0};
    int i = 0, j = 0;
    int max = 0;

    // Find max value and print array
    for (i = 0; i < N; i++) {
        if (max < a[i]) {
            max = a[i];
        }
        printf("%d\t", a[i]);
    }
    printf("\n");

    // Print histogram
    for (i = 0; i < max; i++) {
        for (j = 0; j < N; j++) {
            if (i < a[j]) {
                printf("*");
            }
            printf("\t");
        }
        printf("\n");
    }

    return 0;
}

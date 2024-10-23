#include <stdio.h>
// char str[]="BAAAABBB";
// char res[]="01111111";
// set first char str[0] as current_tile, init count_match=1;
// loop to find next str[i](i =1;i<WIDTH;i++), compare with current_tile
// if strcmp(str[i],current_tile)==0, count_match++, current_tile=str[i];
// else
// if count_match>=3, replace for(int j=i;j>i-count_match;j--){str[i]='.';}, count_match=1;
// else current_tile=str[i],count_match=1;
// current_tile=str[i]
int main(void)
{
    int match_result_matrix[6][5]={0};
    for(int i=0;i<6;i++){
        for(int j=0;j<5;j++){
            printf("%d",match_result_matrix[i][j]);
        }
        printf("\n");
    }
    return 0;
}
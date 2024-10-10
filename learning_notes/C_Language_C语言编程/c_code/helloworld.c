#include <stdio.h>
#include <stdlib.h>

void foo(void)
{
    int i;
    printf("%d\n", i);
    i = 777;
}

int main(int argc,char * argv[])
{
    int x,x1,x2;
    x = 1234;

    system("clear");
    x1 = x % 10;
    x2 = x % 100;
    printf("x1 is %d,  x2 is %d\n",x1,x2);
    
    for ( x = 0; x < argc; x++){
    	printf("%s\n",argv[x]);
    }
    //while(1){
    //}
    return 0;
}

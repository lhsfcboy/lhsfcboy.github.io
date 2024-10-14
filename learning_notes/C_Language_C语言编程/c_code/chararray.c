#include <stdio.h>

int main(){
	char chars1 []  = "hello12345hello";
	char chars2 [4] = "12ii";
	char chars3 [9] = "12345678";

	printf("%s\n",chars1);
	printf("%s\n",chars2);
	printf("%s\n",chars3);
	// 注意观察chars2是如何`入侵`了chars3的领域
	return 0;
}

#include "format.h"
#define PR printf
#define NL "\n"
#define D "%d"


int main(){
	int a = 1,b = 2,c = 3;
	PR (D NL,a);
	PR (D,a);
	
	return 0;
}


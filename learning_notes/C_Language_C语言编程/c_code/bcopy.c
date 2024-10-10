
#include <string.h>
main()
{
	char *s = "Golden Global View";
	char d[20];
	int i;

//	clrscr();		// clear screen
	bcopy(s, d, 6);
	printf("s: %s\n", s);
	printf("d: %s\n", d);


	getchar();
//	clrscr();
	s[13] = 0;
	bcopy(s + 7, d, 11);	// bcopy ignore null in string
	printf("%s\n", s + 7);
	for ( i = 0; i < 11; i++)
		putchar(d[i]);

	getchar();
	return 0;
}

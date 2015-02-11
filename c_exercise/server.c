 /********i*****************
 * server.c server program
 *
 */
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <string.h>
#define PORT (u_short)10000
#define BUF_LEN 100

char hostname[]="tkcoetipoff_98";
char buf[BUF_LEN];

main()
{
	struct hostent *myhost;
	struct sockaddr_in me;
	int	s_waiting,s;

	myhost = gethostbyname(hostname);
	printf ("%s", myhost->h_name);
	
	bzero((char *)&me,sizeof(me));
	me.sin_family = AF_INET;
	me.sin_port = PORT;
	bcopy(myhost->h_addr,
	(char *)&me.sin_addr,myhost->h_length);
	
	printf ("---------------\n");
	s_waiting = socket (AF_INET,SOCK_STREAM,0);
	bind(s_waiting,(struct sockaddr*) &me, sizeof(me));
	printf ("---------------\n");
	listen(s_waiting, 1);
	s = accept(s_waiting, NULL, NULL);
	close (s_waiting);

	write(1, "hello there ! \n", 20);

	do
		{
		int n;
		n = read(0, buf, BUF_LEN);
		write(s, buf, n);
		n = read(s, buf, BUF_LEN);
		write(1, buf, n);
		}
	while(strncmp(buf, "quit", 4)!= 0);
	
	close(s);

	
}

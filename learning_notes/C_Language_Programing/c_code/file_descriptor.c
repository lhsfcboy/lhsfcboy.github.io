main (){
	int fd[4];
	char buf[1000];

	fd[1] = open("start.c", 0);
	fd[2] = open("enum.c", 0);	
	printf("%d    %d\n", fd[1],fd[2]);

	read(fd[1], buf, 1000);
	write(1, buf, 100);
	close(fd[1]);


}

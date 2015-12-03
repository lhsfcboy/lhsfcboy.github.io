#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define HEIGHT 40
#define LENGTH 50


struct node {
	int current;
	int next;
};


struct node nodes[HEIGHT + 2][LENGTH + 2];

void print(void)
{
	int i, j;
	for (j = 0; j <= HEIGHT+1; j++) {
		for (i = 0; i <= LENGTH+1; i++) {
			printf("%d ",nodes[j][i].current);
		}
		printf("\n");
	}
	
	printf("-------------------------------------------------\n");
	
	for (j = 0; j <= HEIGHT+1; j++) {
		for (i = 0; i <= LENGTH+1; i++) {
			printf("%d ",nodes[j][i].next);
		}
		printf("\n");
	}

	printf("-------------------------------------------------\n");
}

void init(void)
{
	srand(time(NULL));
	int i, j;
	for (j = 0; j <= HEIGHT+1; j++) {
		for (i = 0; i <= LENGTH+1; i++) {
			nodes[j][i].current = 1;
			nodes[j][i].next = random() % 2  ;
		}
	}
}

void draw(void)
{
//	sleep(1);
	usleep(1000000);
	system("clear");
	int i, j;
	for (j = 1; j <= HEIGHT; j++) {
		for (i = 1; i <= LENGTH; i++) {
			if (nodes[j][i].current == 1) {
				printf("* ");
			}else{
				printf("  ");
			}
		}
		printf("\n");
	}
	printf("-------------------------------------\n");

}

void new_gen(void)
{
	int i, j;
	for (j = 0; j <= HEIGHT + 1; j++) {
		for (i = 0; i <= LENGTH + 1; i++) {
			nodes[j][i].current = nodes[j][i].next;
			if (j == 0 || j == (HEIGHT + 1) || i == 0
			    || i == (LENGTH + 1)) {
				nodes[j][i].current = 0;
//				printf("j is %d, i is %d,\n",j,i);
//				printf("aji ,ata,a%d%d, is %d\n",j,i,nodes[j][i].current);
			}
		}
	}

//	print();
	int surround;
	for (j = 1; j <= HEIGHT; j++) {
		for (i = 1; i <= LENGTH; i++) {
			surround =
			    nodes[j - 1][i - 1].current + nodes[j -
								1][i].
			    current + nodes[j - 1][i + 1].current +
			    nodes[j][i - 1].current + nodes[j][i + 1].current +
			    nodes[j + 1][i - 1].current + nodes[j +
								1][i].
			    current + nodes[j + 1][i + 1].current;
//			printf("surround is %d,for nodes[%d][%d],   ", surround,j,i);
//			printf("node.current is %d,   ",nodes[j][i].current);
			if (surround == 3) {
				nodes[j][i].next = 1;
			} else if (surround == 2) {
				;
			} else {
				nodes[j][i].next = 0;
//				printf("node[%d][%d] is 0\n",j,i);
			}
//			printf("thus,nodes.next is %d\n",nodes[j][i].next);

		}
	}
//	print();
}

int main(void)
{
	init();
	while (1) {
		draw();
		new_gen();
//		return 0;
	}
	return 0;
}

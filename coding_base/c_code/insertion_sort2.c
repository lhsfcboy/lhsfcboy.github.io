#define LEN 5


int a[LEN]={90,80,10,60,30};
int i,j,temp;


void print_a(){
	printf("a0\ta1\ta2\ta3\ta4\n");
	printf("%d\t%d\t%d\t%d\t%d\n",
		a[0],a[1],a[2],a[3],a[4]);

}

void sort_a(){
	i = 0; j = 0;  temp = 0;
	for(i = 1; i < LEN; i++){
		temp = a[i];
		printf("i is %d,temp is %d--------------\n",i,temp);
		
		for(j=i-1;a[j] > temp;j--){
			a[j+1] = a[j];
		}
		a[j+1]=temp;
		print_a();
	}
	
	
}

int main(){
	print_a();
	sort_a();
	return 0;
}

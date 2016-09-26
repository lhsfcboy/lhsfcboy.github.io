#include<iostream>
using namespace std;

void print(int a, int b, int c,int d,int e,int f,int g)
{
cout << "a=" << a << ",b=" << b << ",c=" << c
<< ",d=" << d << ",e=" << e << ",f=" << f << ",g=" << g << endl;
}

int main(int argc, char*argv[])
{
int x = 1;
print(x++,++x,x++,++x,x++,++x,x++);
cout << "x=" << x << endl;
return 0;
}

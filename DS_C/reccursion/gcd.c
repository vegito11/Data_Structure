// programm of GCD
#include<stdio.h>
int GCD(int a,int b);
int main()
{
      int a,b,g;
      printf("\n Enter the two number:\n\t a = ");scanf("%d",&a); 
      printf("\n\t b = ");scanf("%d",&b);
      g=GCD(a,b);
      printf("\n GCD of  (%d,%d) = %d",a,b,g);
      printf("\n\n");
      return 0;
}

int GCD(int a,int x)
{
      if(a==0)
      return x;
      else if(x==0)
      return a;
      else if(a>x)
      return GCD(a%x,x);
      else if(x>a)
      return GCD(a,x%a);
}

/*output
       Enter the two number:
	 a = 56

	 b = 12

 GCD of  (56,12) = 4

*/

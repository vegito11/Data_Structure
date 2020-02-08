//programm of factorial of number
#include<stdio.h>
int fact(int );
int main()
{
      int n,f;
      printf("\n Enter a number :");
      scanf("%d",&n);
      f=fact(n);
      printf("\n Factorial of %d  is : %d ",n,f);
      printf("\n\n");
      return 0;
}

int fact(int x)
{
      if(x==1)
      return 1;
      else
      return (x*fact(x-1));
}

/*output

 Enter a number :5

 Factorial of 5  is : 120 

*/


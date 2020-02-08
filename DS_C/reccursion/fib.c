//programm of fib series
#include<stdio.h>
int fib(int );
int main()
{
      int n,f,i;
      printf("\n Enter a number : ");
      scanf("%d",&n);
      printf("\n The Series of %d Fibbo Number is : ",n);
      for(i=0;i<n;i++)
      {
            f=fib(i);
            printf("\t%d",f);
      }
      printf("\n\n");
      return 0;
}

int fib(int x)
{
      if(x==1||x==2)
      return 1;
      else if(x==0)
      return 0;
      else
      return(fib(x-1)+fib(x-2));
}

/*output
 Enter a number : 8

 The Series of 8 Fibbo Number is : 	0	1	1	2	3	5    8	13
 */



#include<stdio.h>
#include<stdlib.h>

int main()
{
      int a[5],i,j,tmp;
      printf("\n Enter the elment in array :");
      for(i=0;i<5;i++)
      {
            scanf("%d",&a[i]);
      }
      printf("\n The element in array before sorting :");
      for(i=0;i<5;i++)
      {
            printf("%4d",a[i]);
      }
      for(i=0;i<5;i++)
      {
            for(j=0;j<4-i;j++)
            {
                  if(a[j]<a[j+1])
                  {
                        tmp=a[j];
                        a[j]=a[j+1];
                        a[j+1]=tmp;
                  }
            }
      }
      printf("\n The element in array after sorting :");
      for(i=0;i<5;i++)
      {
            printf("%4d",a[i]);
      }
      printf("\n\n");
      return 0;
}


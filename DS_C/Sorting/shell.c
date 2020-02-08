#include<stdio.h>
#include<stdlib.h>

void shellsort(int a[],int n)
{
      int gap,j,i,tmp;
      for(gap=n/2;gap>0;gap=gap/2) 
      {
            for(i=gap;i<n;i++)
            {
                  tmp=a[i];
                  for(j=i;j>=gap && a[j-gap]>tmp;j=j-gap)
                  {
                        a[j]=a[j-gap];
                  }
                  a[j]=tmp;
            }
      }
}

int main()
{
      
      int a[10],i,j,tmp,n;
      printf("\n Enter the elment in array :");
      //n=SIZE;      
      for(i=0;i<10;i++)
      {
            scanf("%d",&a[i]);
      }
      
      printf("\n The element in array before sorting :");
      for(i=0;i<10;i++)
      {
            printf("%4d",a[i]);
      }
      shellsort(a,10);
      printf("\n The element in array After sorting  :");
      for(i=0;i<10;i++)
      {
            printf("%4d",a[i]);
      }
      printf("\n");
      return 0;
} 

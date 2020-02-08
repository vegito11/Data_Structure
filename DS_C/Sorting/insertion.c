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
      for(i=1;i<5;i++)
      {
            tmp=a[i];
            j=i-1;            
            while(j>=0&&a[j]>tmp)
            {
                  a[j+1]=a[j];  // shift
                  j--;
            }
            a[j+1]=tmp;       //jth +1 means 0 if tmp is smallest element i.e. tmp will be at it suitable position
            
      }
      printf("\n The element in array after  sorting :");
      for(i=0;i<5;i++)
      {
            printf("%4d",a[i]);
      }
      printf("\n\n");
      return 0;
}


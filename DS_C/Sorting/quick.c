#include<stdio.h>
#include<stdlib.h>
#define SIZE 5
void swap(int *a,int*b)
{
      int tmp;
      tmp=*a;
      *a=*b;
      *b=tmp;
}
int partition(int a[],int low,int high)
{
      int i,j,pivot;
      pivot=a[high];
      i=low-1;
      for(j=low;j<=high-1;j++)      
      {
            if(a[j]<=pivot)
            {
                  i++;
                  swap(&a[i],&a[j]);
            }
      }
      swap(&a[i+1],&a[high]);
      return i+1;
}

void quick(int a[],int low,int high)
{
      if(low<high)
      {
            int pi=partition(a,low,high);
            quick(a,low,pi-1);
            quick(a,pi+1,high);
            
      }
}


int main()
{
      
      int a[SIZE],i,j,tmp,n;
      printf("\n Enter the elment in array :");
      //n=SIZE;      
      for(i=0;i<SIZE;i++)
      {
            scanf("%d",&a[i]);
      }
      
      printf("\n The element in array before sorting :");
      for(i=0;i<SIZE;i++)
      {
            printf("%4d",a[i]);
      }
      quick(a,0,SIZE-1);
      printf("\n The element in array After sorting  :");
      for(i=0;i<SIZE;i++)
      {
            printf("%4d",a[i]);
      }
      printf("\n");
      return 0;
}

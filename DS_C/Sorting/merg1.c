#include<stdio.h>
#include<stdlib.h>
#define SIZE 5

void merge(int a[],int a1start,int a2start,int end)
{
      int i,j,k,a1size,a2size;
      a1size= a2start-a1start+1;
      a2size=end-a2start;
      int L[a1size],R[a2size];
      for(i=0;i<a1size;i++)
      {
            L[i]=a[a1start+i];
      }
      for(j=0;j<a2size;j++)
      {
            R[j]=a[a2start+1+j];
      }
      i=0;j=0;k=a1start;  
      while(i<a1size && j<a2size)
      {
            if(L[i]<=R[j])
            {
                  a[k]=L[i];
                  i++;
            }
            else
            {
                  a[k]=R[j];
                  j++;
            }
            k++;
      }
            while(i<a1size)
            {
                  a[k]=L[i];
                  i++;
                  k++;
            }
            while(j<a2size)
            {
                  a[k]=R[j];
                  j++;
                  k++;
            }
}
void sort(int a[],int start,int size)
{
      if(start<size)
      {
            int m=start+(size-start)/2;
            sort(a,start,m);
            sort(a,m+1,size); 
            merge(a,start,m,size);
      }            
}


int main()
{
      int a[SIZE],i,j,tmp;
      printf("\n Enter the elment in array :");
      for(i=0;i<SIZE;i++)
      {
            scanf("%d",&a[i]);
      }
      printf("\n The element in array before sorting :");
      for(i=0;i<SIZE;i++)
      {
            printf("%4d",a[i]);
      }
      sort(a,0,SIZE);
      printf("\n The element in array after  sorting :");
      for(i=0;i<SIZE;i++)
      {
            printf("%4d",a[i]);
      }
      printf("\n\n");
      return 0;
}


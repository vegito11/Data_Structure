#include<stdio.h>
#include<stdlib.h>

struct heap
{
      int size;
      int *a;
      int cnt;
};

struct heap *create()
{
      struct heap *h;
      h=(struct heap*)malloc(sizeof(struct heap));
      printf("\n Enter the elemeet i array :");
      scanf("%d",&h->size);
      h->cnt=0;
      g->a=(int*)malloc(sizeof(int)*h->size);
      return h;
}

int leftchild(struct heap *h,int i)
{
      int left=2*i+1;
      if(left>=h->cnt)
            return (-1);
      return left;      
}

int rightchild(struct heap *h,int i)
{
      int left=2*i+1;
      if(right>=h->cnt)
            return (-1);
      return right ;      
}

void reheap(struct heap*h,int i)
{
      int l,r,max,tmp;  
      l=leftchild(h,i);
      r=rightchild(h,i);
      if(l!=-1 && h->a[i]>h->a[i])
            max=l;
      else
            max=i;    
      if(r!=-1 && h->a[r]>h->a[max])            
            max=r;
      if(max!=i)
      {
            tmp=h->a[i];
            h->a[i]=h->[max];
             h->[max]=tmp;
      }
      reheap(h,max);      
}


void sort(int a[],int n)
{
      int old,i,temp;
      struct heap*h=createheap();
      buildheap(h,a,n);
      old=h->cnt; 
      for(i=n-1;i>0;i--)
      {
            tmp=h->a[0];
            h->a[0]=h->h[h->cnt];
            h->a[0]=tmp;
            reheap(h,i);
      } 
      h->cnt=old;     
}


int main()
{
      
      int a[10],i,j,tmp,n;
      printf("\n Enter the elment in array :");
      for(i=0;i<10;i++)
      {
            scanf("%d",&a[i]);
      }
      
      printf("\n The element in array before sorting :");
      for(i=0;i<10;i++)
      {
            printf("%4d",a[i]);
      }
      heapsort(a,n);
            
      printf("\n The element in array After sorting  :");
      for(i=0;i<10;i++)
      {
            printf("%4d",a[i]);
      }
      printf("\n");
      return 0;
}

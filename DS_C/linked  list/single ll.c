#include<stdlib.h>
#include<stdio.h>

struct node
{
      int data;
      struct node *link;
};
struct node* start=NULL;
int cnt=0;
struct node* createnode()
{
      struct node* tmp;
      tmp=(struct node*)malloc(sizeof(struct node*));
      tmp->link=NULL;
      return tmp;
}

void insert()
{
      int ch,n,i,pos;
      struct node* tmp,*search;
      
      tmp=createnode();
      printf("\n Enter number to be insert :");
      scanf("%d",&n);
      tmp->data=n;
      if(start==NULL)
      {
            start=tmp;
            cnt++;
            return;
      }
            
      printf("\n\t\t To INSERT At : ");
      printf("\n\t\t\t 1 . Beginning \n\t\t\t 2 . Middle \n\t\t\t 3 . END")
      printf("\n\t\t\t 4 . Location ");
      printf("\t\t Your Choice : ");
      scanf("%d",&ch);
      switch(ch)
      {
          case 1:
                   tmp->link=start;
                   start=tmp;            
                   break;
          case 2:
                   pos=cnt/2;
                   if(pos%2==1)
                   pos+=1;
                   if(pos==1)
                   {
                         tmp->link=start;
                         start=tmp;         
                         cnt++;
                         return;   
                   }
                   search=start;
                   for(i=1;i<pos;i++)
                   {
                               search=search->link;
                   }
                   tmp->link=search->link;
                   search->link=tmp;
                   break;
         case 3:
                   search=start;
                   while(search->link!=NULL)
                   {
                         search=search->link;
                   }
                   search->link=tmp;
                   break;
         case 4:
                  printf("\n\t\t Enter the Location :");
                  scanf("%d",&pos);
                  if(pos==1)
                  {
                        tmp->link=start;
                        start=tmp;         
                        cnt++;
                        return;   
                  }
                  else if(pos>cnt+1)
                  {
                        printf("\n!!!!!!!!!! Please give valid location !!!!!!!!");
                        return;
                  }
                  else
                  {
                        search=start;
                        for(i=1;i<pos-1;i++)
                        {
                                    search=search->link;
                        }
                        tmp->link=search->link;
                        search->link=tmp;
                  }      
                  break;
      }
      cnt++;
      
}               

void delete()
{
      
      struct node* tmp,*search,*last;
      int ch,n,i,pos;
      if(start==NULL)
      {
            printf("\n Sorry LIST is Empty !!!!!! First Insert some Data :)");
            return;
      }
      
      printf("\n\t\t DELETE Node From : ");
      printf("\n\t\t\t 1 . Beginning \n\t\t\t 2 . Middle \n\t\t\t 3 . END \n\t\t\t 4 . Location ");
      printf("\t Your Choice : ");
      scanf("%d",&ch);
      
      switch(ch)
      {
       case 1:
                   tmp=start;
                   start=start->link;
                   printf("\n %d Number is Deleted from list !!!!!!",tmp->data);
                   free(tmp);
                   break;
       case 2:
                   pos=cnt/2;
                   printf("%d",pos);
                   if(cnt%2==1)
                   {
                         pos+=1;
                   }     
                   if(pos==1)
                   {
                         tmp=start;
                         start=start->link;
                         free(tmp);
                         cnt--;
                         return ;
                   }
                   search=start;
                   for(i=1;i<pos-1;i++)
                   {
                         search=search->link;
                   }
                   tmp=search->link;
                   search->link=tmp->link;
                   printf("\n %d Number is Deleted from list !!!!!!",tmp->data);
                   free(tmp);
                   break;
       case 3:
                   search=start;
                   while(search->link!=NULL)
                   {
                         last=search;            //point to last-1 node i.e is future last
                         search=search->link;
                   }
                   tmp=search;
                   last->link=NULL;
                   printf("\n %d Number is Deleted from list !!!!!!",tmp->data);
                   free(tmp);
                   tmp=NULL;
                   break;
       case 4:
                   printf("\n Enter the Location :");
                   scanf("%d",&pos);
                   if(pos==1)
                   {
                         tmp=start;
                         start=start->link;
                         printf("\n %d Number is Deleted from list !!!!!!",tmp->data);
                         free(tmp);
                         cnt--;
                         return ;
                   }
                   else if(pos>cnt)
                   {
                         printf("\n Please give valid location !!!!!!!!");
                         return;
                   }
                   else
                   {
                         search=start;
                         for(i=1;i<pos-1;i++)
                         {
                                     search=search->link;
                         }
                         tmp=search->link;
                         search->link=tmp->link;
                         printf("\n %d Number is Deleted from list !!!!!!",tmp->data);
                         free(tmp);
                   }
                   break;
      }
      cnt--;
      
}

void dis()
{
            struct node* tmp;
            tmp=start;
            if(start==NULL)
            {
                  printf("\n Sorry LIST is Empty !!!!!! First Insert some Data :");
                  return;
            }
            printf("\n List is : ");
            while(tmp!=NULL)
            {
                  printf("%5d",tmp->data);
                  tmp=tmp->link;
            }
}   

void count()
{
       printf("\n Count of number of Nodes is : %d",cnt);      
}            

int main()
{
      int ch;
      while(1)
      {
            printf("\n\n******** Enter your choice********* :");
            printf("\n\t 1. INSERT \n\t 2. DELETE \n\t 3. DISPLAY \n\t 4. COUNT \n\t 5. EXIT");
            printf("\n Enter Your Choice :...");
            scanf("%d",&ch);
            if(ch>4)
            break;
            switch(ch)
            {
                  case 1:
                        insert();
                        break;
                  case 2:
                        delete();
                        break;      
                  case 3:
                        dis();
                        break;      
                  case 4:
                        count();

            }
     }       
      return 0;
}


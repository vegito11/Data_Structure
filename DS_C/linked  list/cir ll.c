#include <stdlib.h>
#include <stdio.h>

struct node
{
      int data;
      struct node *next;
};
struct node* start=NULL;
struct node* last=NULL;
int cnt=0;
struct node* createnode()
{
      struct node* tmp;
      tmp=(struct node*)malloc(sizeof(struct node*));
      tmp->next=NULL;
      return tmp;
}

void insert()
{
      int ch,n,i,pos;
      struct node* tmp,*search,*mid;
      
      tmp=createnode();
      printf("\n Enter number to be insert :");
      scanf("%d",&n);
      tmp->data=n;
            
            if(start==NULL)
            {
                  start=tmp;
                  last=tmp;
                  cnt++;
                  return;
            }
            
            printf("\n\t\t To INSERT At : ");
            printf("\n\t\t\t 1 . Beginning \n\t\t\t 2 . Middle \n\t\t\t 3 . END \n\t\t\t 4 . Location ");
            printf("\t\t Your Choice : ");
            scanf("%d",&ch);
            switch(ch)
            {
                  case 1:
                              tmp->next=start;
                              start=tmp;
                              last->next=tmp;
                              break;
                  case 2:
                              pos=cnt/2;
                              if(pos%2==1)
                              {
                                          pos+=1;
                              }           
                              if(pos==1)
                              {
                                    tmp->next=start;
                                    start=tmp;
                                    last->next=tmp;
                                    cnt++;
                                    return;   
                              }
                               search=start;
                               for(i=1;i<pos-1;i++)
                               {
                                     search=search->next;    //n-1th node
                               }
                               tmp->next=search->next;
                               search->next=tmp;       //nth node prev
                              break;
                  case 3:
                              last->next=tmp;
                              last=tmp;
                              last->next=start;            
                              break;
                  case 4:
                              printf("\n\t\t Enter the Location :");
                              scanf("%d",&pos);
                              if(pos==1)
                              {
                                    tmp->next=start;
                                    start=tmp;
                                    last->next=tmp;
                                    cnt++;
                                    return;   
                              }
                              else if(pos>cnt+1)
                              {
                                    printf("\n!!!!!!!!!! Please give valid location !!!!!!!!");
                                    return;
                              }
                              else if(pos==cnt)
                              {
                                    last->next=tmp;
                                    last=tmp;
                                    last->next=start;            
                              }
                              else
                              {
                                    search=start;
                                    for(i=1;i<pos-1;i++)
                                    {
                                                search=search->next;    //n-1th node
                                    }
                                    tmp->next=search->next;
                                    search->next=tmp;       //nth node prev
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
                              start=start->next;
                              last->next=start;
                              printf("\n %d Number is Deleted from list !!!!!!",tmp->data);
                              free(tmp);
                              break;
                  case 2:
                              pos=cnt/2;
                              if(cnt%2==1)
                              {
                                    pos+=1;
                              }     
                              if(pos==1)
                              {
                                    tmp=start;
                                    start=start->next;
                                    last->next=start;
                                    printf("\n %d Number is Deleted from list !!!!!!",tmp->data);
                                    free(tmp);
                                    cnt--;
                                    return ;
                              }
                              search=start;
                              for(i=1;i<pos-1;i++)
                              {
                                          search=search->next;
                              }
                              tmp=search->next;
                              search->next=tmp->next;
                              printf("\n %d Number is Deleted from list !!!!!!",tmp->data);
                              free(tmp);
                              break;
                  case 3:
                              search=start;
                              while(search->next!=NULL)
                              {
                                    last=search;      
                                    search=search->next;
                              }
                              last->next=NULL;      
                              tmp=search;
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
                                    start=start->next;
                                    last->next=start;
                                    printf("\n %d Number is Deleted from list !!!!!!",tmp->data);
                                    free(tmp);
                                    cnt--;
                                    return;
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
                                                search=search->next;    
                                    }
                                    tmp=search->next;
                                    search->next=tmp->next;
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
            while(tmp->next!=start)
            {
                  printf("%5d",tmp->data);
                  tmp=tmp->next;
            }
                  printf("%5d",tmp->data);            
            printf("\n");
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
            printf("\n\n******** Enter your choice********* :\n\t 1. INSERT \n\t 2. DELETE \n\t 3. DISPLAY \n\t 4. COUNT \n\t 5. EXIT");
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


#include<stdio.h>
void toh(int ,char,char,char);
int main()
{
      int cnt;
      printf("\n Enter the count of disk is :");
      scanf("%d",&cnt);
      toh(cnt,'A','C','B');
      printf("\n\n");
      return 0;
}
void toh(int cnt,char A,char B,char C)
{
     void toh(int n, char f, char t, char a)
{
    if (n == 1)
    {
        printf("\n Move disk 1 from rod %c to rod %c", f, t);
        return;
    }
    toh(n-1, f, a, t);
    printf("\n Move disk %d from rod %c to rod %c", n, f, t);
    toh(n-1, a, t, f);
}
}

/*Output

*/

#include <stdio.h>
int myfunc();
int main(int argc, char const *argv[])
{
    int my_arr[10]={10};
    //fill with numbers
    for (int i = 0; i < 10; i++)
    {
        my_arr[i] = i;
    }
    
    printf("Hello World");
    myfunc(my_arr);
    return 0;
}


int myfunc(int myar[]) {
    int count = 0;
    printf("\r\n");
    for (int i = 0; i < sizeof(*myar); i++)
    {
        printf("%d\r\n",myar[i]);
    }
    
    while(count<4)
    {
    printf("%d)Hello\r\n", count);
    count++;
    }
    
    return 1;
}
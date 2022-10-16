#include <stdio.h>

int main(void)
{
    int first,sec,third,one=1,two=2,three=3,a,b;
    printf("please enter three numbers:");
    scanf("%d%d%d",&first,&sec,&third);
    if (first==one){
        a++;
    }
    if (sec==one){
        b++;
    }
    if (third==one){
        b++;
    }
    if (first==two){
        b++;
    }
    if (sec==two){
        a++;
    }
    if (third==two){
        b++;
    }
    if (first==three){
        b++;
    }
    if (sec==three){
        b++;
    }
    if (third==three){
        a++;
    }
    else{
        printf("None");
    }

    printf("%dA,%dB",a,b);
    if (a==3){
        printf("Bingo");
    }
    return 0;
}

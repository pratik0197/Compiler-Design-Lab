#include<stdio.h>
#include<string.h>
#include<stdbool.h>
int dfa[4][2];
int contains_even_ones_and_odd_zeroes(char s[]){
    int n = strlen(s);
    int state = 0;
    printf("The states of the string in the DFA are : ");
    for(int i=0;i<n;i++){
        state = dfa[state][s[i]-'0'];
        printf("%d ",state);
    }
    printf("\n");
    return state == 3;
}
int main(){
    dfa[0][0] = dfa[2][1] = 3;
    dfa[1][0] = dfa[3][1] = 2;
    dfa[2][0] = dfa[0][1] = 1;
    dfa[3][0] = dfa[1][1] = 0;
    char str[1000];
    printf("Enter the String(Binary String) : ");
    scanf("%s",str);
    printf("%s\n",(contains_even_ones_and_odd_zeroes(str)?"String was Accepted" :"String was rejected"));
}

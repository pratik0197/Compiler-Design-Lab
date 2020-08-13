%{
#include<string.h>
#include<stdio.h>
char s[101];

void operator(int *k,char s[],int n){
    char aux[n+1];
    for(int i=0;i<n;i++)
        aux[i] = s[i];
    aux[n] = '\0';
    int a = *k;
    if(strcmp(aux,"ONE") == 0)
        a++;
    else if(strcmp(aux,"TWO") == 0)
        a+=2;
    else if(strcmp(aux,"THREE") == 0)
        a+=3;
    else if(strcmp(aux,"FOUR") == 0)
        a+=4;
    else if(strcmp(aux,"FIVE") == 0)
        a+=5;
    else if(strcmp(aux,"SIX") == 0)
        a+=6;
        
    else if(strcmp(aux,"SEVEN") == 0)
        a+=7;
    else if(strcmp(aux,"EIGHT") == 0)
        a+=8;
        
    else if(strcmp(aux,"NINE") == 0)
        a+=9;
    
    else if(strcmp(aux,"TEN") == 0)
        a+=10;
        
    else if(strcmp(aux,"ELEVEN") == 0)
        a+=11;

    else if(strcmp(aux,"TWELVE") == 0)
        a+=12;
    else if(strcmp(aux,"THIRTEEN") == 0)
        a+=13;
    else if(strcmp(aux,"FOURTEEN") == 0)
        a+=14;
    else if(strcmp(aux,"FIFTEEN") == 0)
        a+=15;
    else if(strcmp(aux,"SIXTEEN") == 0)
        a+=16;
    else if(strcmp(aux,"SEVENTEEN") == 0)
        a+=17;
        
    else if(strcmp(aux,"EIGHTEEN") == 0)
        a+=18;
    else if(strcmp(aux,"NINETEEN") == 0)
        a+=19;
    else if(strcmp(aux,"TWENTY") == 0)
        a+=20;
        
    else if(strcmp(aux,"THIRTY") == 0)
        a+=30;
        
    else if(strcmp(aux,"FORTY") == 0)
        a+=40;
        
    else if(strcmp(aux,"FIFTY") == 0)
        a+=50;
        
    else if(strcmp(aux,"SIXTY") == 0)
        a+=60;
        
    else if(strcmp(aux,"SEVENTY") == 0)
        a+=70;
        
    else if(strcmp(aux,"EIGHTY") == 0)
        a+=80;
        
    else if(strcmp(aux,"NINETY") == 0)
        a+=90;
        
    else if(strcmp(aux,"HUNDRED") == 0)
        a = a*100;
    *k  = a;
}
%}
%%
    char cache[100];
    int idx = 0;
    int ans = 0;
    int n = strlen(s);
    for(int i=0;i<n;i++){
        if(s[i]==' '){
            if(idx!=0)
                operator(&ans,cache,idx);
            idx = 0;
        }else{
            cache[idx++] = s[i];
        }
    }
    operator(&ans,cache,idx);
    printf("%d\n",ans);
    {return 5;}
%%
int yywrap(){
    return 0;
}
int main(){
    gets(s);
    yylex();
}

/*
    INPUT :: ONE HUNDRED NINETY SEVEN
    OUTPUT :: 197
*/

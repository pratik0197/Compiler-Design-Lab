%{ 
#include <stdio.h>
#include <string.h>
char s[1000];
%} 
  
%% 
	
	int dfa[256][3];
	for(int i=0;i<256;i++)
	{
		dfa[i][0] = 2;
		dfa[i][1] = 2;
		dfa[i][2] = 2;
	}
	for(int i='a';i<='z';i++)
	{
		dfa[i][0] = 1;
		dfa[i][1] = 1;
	}
	for(int i='A';i<='Z';i++)
	{
		dfa[i][0] = 1;
		dfa[i][1] = 1;
	}
	for(int i='0';i<='9';i++){
		dfa[i][0] = 2;
		dfa[i][1] = 1;
	}
	dfa['_'][0] = dfa['_'][1] = 1;
	int state = 0;
	int n = strlen(s);
	for(int i=0;i<n;i++)
		state = dfa[s[i]][state];
	if(state !=1 )
		return 0;
	else
		return 1;
%%
int yywrap(){
	return 1;
}
int main()
{
	while(1)
	{
		scanf("%s",s);
		int k  = yylex();
		if(k == 1)
			printf("Valid Indentifier\n");
		else
			printf("Invalid Indentifier\n");
	}
return 0;
}

%{
    /* definitions */
%}

%%
    /* rules */
[a-z] {printf("Single lowercase char\n");}
. {printf("Not a Single lowercase char\n");}
\n {return 0;}

%%

yywarp(){};

int main(){
    printf("Enter string: ");
    yylex();

    return 0;
}
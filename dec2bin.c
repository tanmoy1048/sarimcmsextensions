#include<stdio.h>
#include<math.h>
int main() {
int dec,a,v,k=0,lt;
int bin[80];
printf("Enter the decimal number : ");
scanf("%d",&dec);
a = dec;
lt = log ( dec ) / log (2);
for (k = 0 ; k <= lt ; k++){
v = a % 2;
bin[k] = v;
a = a / 2 ;
}
printf("\nThe binary value of %d is ",dec);
for (k;k!=0;k=k-1) printf("%d",bin[k-1]);
printf("\n\nThank You\n");
return 0 ;
}

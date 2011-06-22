#include<stdio.h>

int main() {
int dec,a,v,k=0;
int bin[80];
printf("Enter the decimal number : ");
scanf("%d",&dec);
a = dec;
do {
v = a % 2;
bin[k] = v;
a = a / 2 ;
k++; } while (a > 0);
printf("\nThe binary value of %d is ",dec);
for (k;k!=0;k=k-1) printf("%d",bin[k-1]);
printf("\n\nThank You\n");
return 0 ;
}

/* La definicion de un numero
   par se define como n%2 = 0 */
#include<stdio.h>
int main(){
	int n;
	
	printf("Ingrese un valor: ");
	scanf("%d",&n);
	
	if(n%2 == 0){
		printf("%i es par\n",n);
	}else{
		printf("%i es impar\n",n);
	}
	return 0;
}

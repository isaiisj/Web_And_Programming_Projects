#include<stdio.h>
int main(){
	int a,b;
	double cociente;
	
	printf("Ingrsese dos valores: ");
	scanf("%i %i",&a,&b);
	//verifico si el denominador es cero
	if( b==0 ){
		printf("Error l, no puedo dividir entre cero\n");
	}else{
		cociente = (double)a/b; //type casting o casting
		printf("%d / %d = %lf\n",a,b,cociente);
	}
	return 0;
}


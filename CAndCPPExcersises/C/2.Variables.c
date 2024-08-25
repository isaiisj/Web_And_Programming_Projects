#include<stdio.h>
int main(){
	char nombre[20];
	int edad;
	double altura;
	
	printf("Ingrese su nobre: ");
	scanf("%s",nombre);//string no se referencian con & 
	
	printf("Ingrese su edad: ");
	scanf("%i",&edad);
	
	printf("Ingrese su altura: ");
	scanf("%lf",&altura);
	
	printf("Ud. es %s, tiene %d años y una altura de %lf\n",nombre,edad,altura);
	return 0;
}

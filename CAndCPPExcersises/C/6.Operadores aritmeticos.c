/*Programa que te dice fecha cuan ingresas un numero
  de 8 digitos por aaaammdd*/
#include<stdio.h>
int main(){
	long f;
	int dia, mes, anio;
	int resto;
	
	printf("Ingrese una fecha: ");
	scanf("%li", &f);
	//La division entre enteros tambien lo sera
	anio = f/10000;
	resto = f%10000;
	
	mes = resto/100;
	dia = resto%100;
	
	printf("Dia: %d\n",dia);
	printf("Mes: %i\n",mes);
	printf("Año: %d\n",anio);
	return 0;
}

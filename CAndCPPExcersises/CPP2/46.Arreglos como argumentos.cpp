#include <iostream>
#include <iomanip>

using namespace std;

int const LONGUITUD = 5;
int const FILAS = 3;
int const COLUMNAS = 3;

void mostrarArreglo (int[LONGUITUD]);
void ordenarArreglo (int [LONGUITUD]);

mostrarArreglo(matriz);

int main()
{
    
    int numeros(LONGUITUD) = {3,4,6,5,9};
    int matriz[FILAS][COLUMNAS] = {{5,2,4},{8,9,4},{12,2,0}};
    
    mostrarArreglo(numeros);
    ordenarArreglo(numeros);
    mostrarArreglo(numeros);
    
    system("pause");
    return 0;
    
}
void ordenarArreglo (int arreglo[LONGUITUD]
{
     int i,j;
     
     for(i=1;i < LONGUITUD; i++)
     {
               for(j=0;j < LONGUITUD - i; j++)
               {
                         if(arreglo[j] > arreglo[j+1])
                         {
                                       aux = arreglo[j];
                                       arreglo[j] = arreglo[j+1];
                                       arreglo[j+1] = aux;
                                       }
                         }
               }
     }
                                       
void mostrarArreglo (int arreglo[LONGUITUD])
{
     int i;
     
     for(i=0;i < LONGUITUD; i++)
     {
                         cout << setw(4) << arreglo[i];
               }
               cout << "\n\n" << endl;

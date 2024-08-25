#include<iostream>
using namespace std;
void multiplicar(int,int);
void cuadrado(int);
int main()
{
    multiplicar(5,4);
    cuadrado(8);
    system("pause");
    return 0;
}
void multiplicar(int x,int y)
{
     cout << x*y << endl;
}
void cuadrado(int x)
{
     cout << "La funcion cuadrado recibio el argumento " << x << endl;
}

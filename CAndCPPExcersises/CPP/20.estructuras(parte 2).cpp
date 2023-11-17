#include<iostream>

using namespace std;

int main()
{
    struct Hogar 
    {
           int numeroDireccion;
           int numerotel;
           Hogar(){numeroDireccion = 0; numerotel = 2;}
           int verDir(){return numeroDireccion;}
           int guardarDir(int a){numeroDireccion = a;}
           }Fernandez, Gonzalez, perez;
           Fernandez.numerotel = 1034;
           Fernandez.numeroDireccion = 324;
           
           Gonzalez = Fernandez;
           cout << Gonzalez.numerotel << endl;
           cout << perez.numerotel << endl;
           perez.guardarDir(156);
           cout << perez.verDir() << endl;
    cin.get();
    return 0;
}

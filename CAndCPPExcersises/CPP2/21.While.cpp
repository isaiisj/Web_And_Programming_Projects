#include<iostream>
using namespace std;

int main()
{
    int opcion;
    bool opcion_valida = false;
    while( ! opcion_valida){
    cout << "1) Realizar llamada \n"
         << "2) Libreta de telefonos \n"
         << "3) Configuracion \n";
    cin >> opcion;
    switch(opcion)
    {
                  case 1:
                       cout << "Se realiza una llamada\n";
                       opcion_valida = true;
                       break;
                  case 2:
                       cout << "Se busca un telefono\n";
                       opcion_valida = true;
                       break;
                  case 3:
                       cout << "Configuracion\n";
                       opcion_valida = true;
                       break;
                  default:
                          cout << "La opcion ingresada no es valida" << endl;
    }
}
    system("pause");
    return 0;
}

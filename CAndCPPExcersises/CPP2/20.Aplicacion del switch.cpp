#include<iostream>
using namespace std;

int main()
{
    int opcion;
    cout << "1) realizar llamada \n"
         << "2) libreta de telefonos \n"
         << "3) configuracion \n";
         
         cin >> opcion;
         
         switch(opcion)
         {
                       case 1:
                            cout << "Se realiza una llamada";
                            break;
                       case 2:
                            cout << "se busca un telefono";
                            break;
                       case 3:
                            cout << "Configuracion";
                            break;
                       default:
                               cout << "La opcion ingresada no es valida" << endl;
         }
    system("pause");
    return 0;
}

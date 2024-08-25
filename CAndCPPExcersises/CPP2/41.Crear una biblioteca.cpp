#include<iostream>
using namespace std;
namespace ValidacionIngreso
{
          
int tomarInt ();
bool tipoIntValido (string);


int main()
{
    int numero;
    numero = tomarInt();
    cout << "\nEl entero ingresado es: " << numero << endl;
    
    system("pause");
    return 0;
}
int tomarInt ()
{
    string numero;
    bool esValido = false;
    
    while(! esValido)
    {
            try
            {
                     cout << "Ingrese un entero entre 0 y 9: " ;
                     getline(cin,numero);
                     esValido = tipoIntValido(numero);
                     
                     if(! esValido)
                     throw numero;
            }
            catch(string e)
            {
                         cout << "\nEl entero " <<  e << " no es valido " << endl;
            }
    }
    return atoi(numero.c_str());
}
bool tipoIntValido (string numero)
{
     int inicio = 0;
     
     if(numero.length() == 0)
     return 0;
     
     if (numero [0] == '+'  || numero [0] == '-')
     {
                inicio = 1;
                if(numero.length() == 1)
                return 0;
     }
     for(i = inicio ;i < numero.length(); i++)
     {
           if(! isdigit(numero[i]))
           return 0;
     }
     return 1;
}

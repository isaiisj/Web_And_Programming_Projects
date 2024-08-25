#include<iostream>
using namespace std;

int main()
{
    int numerador,denominador;
    try
    {
    cout << " numerador: " << endl;
    cin >> numerador;
    
    cout << " Denominador: " << endl;
    cin >> denominador;
    
    if(denominador == 0)
    throw denominador;
    else
        cout << " El resultado es: " << numerador/denominador << endl;
    }
        
    catch (int e)
    {
          cout << " El denominador " << e << " no es valido. " << endl;
    }
    
    system("pause");
    return 0;
}

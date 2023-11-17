#include<iostream>

using namespace std;

int numero = 12;
int *puntero = &numero;
int main()
{
    cout<< *puntero << endl;
    cin.get();
    return 0;
}

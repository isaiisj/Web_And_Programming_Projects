#include<iostream>
using namespace std;

template <class T>
void cuadrado (T);

int main ()
{
    cuadrado(5);
    
    system("pause");
    return 0;
}
template <class T>
void cuadrado (T x)
{
     cout << " El cuadrado de " << x << " es " << x*x << endl;
}

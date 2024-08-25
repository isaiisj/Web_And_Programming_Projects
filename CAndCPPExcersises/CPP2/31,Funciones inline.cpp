#include<iostream>
using namespace std;

inline int cubo (int);
int main()
{
    int numero = 6;
    cout << " El cubo de numero " << numero  << " es " << cubo (numero) << endl;
    system("pause");
    return 0;
}
inline int cubo (int x)
{
       return (x * x * x);
}

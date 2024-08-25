#include<iostream>
using namespace std;

int main()
{
    int p;
    double temperaturas [4] = {37.5,36,35,36.5};
    char caracteres [] = "palabra".c_str()
    cout << "El arreglo ingresado[ " ;
    
    for(p=0; p < CANTIDAD; p++)
    cout << temperaturas[p] << " ";
    
    cout << " ] ";
    system("pause");
    return 0;
}

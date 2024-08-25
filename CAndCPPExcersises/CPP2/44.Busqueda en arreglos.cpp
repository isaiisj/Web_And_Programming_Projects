#include<iostream>
using namespace std;

int main()
{
    const int LONGUITUD = 5;
    int lista[LONGUITUD] = {3,1,8,2,5} ;
    bool dos = false;
    int i;
    
    for(i=0; i < LONGUITUD; i++)
    {
             if(lista[i] == 2)
             dos = true;
    }
    
    if (dos)
    cout << "El elemento 2 se encuentra en el arreglo " << endl;
    else
    cout <<"El elemento 2 no se encuentra en el arreglo " << endl;
             
    system("pause");
    return 0;
}

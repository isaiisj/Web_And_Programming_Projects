#include<iostream>
using namespace std;

int main()
{
    const int LONGUITUD = 5;
    int lista[LONGUITUD] = {3,1,8,2,5} ;
    int i,j;
    int aux;
    
    for(i = 1; i < LONGUITUD; i++){
          for(j = 0; j < LONGUITUD-i; j++){
                if(lista[j] > lista[j+1]){
                            aux = lista[j];
                            lista[j] = lista[j+1];
                            lista[j+1] = aux;
                }
          }
    }
    for(i = 0; i < LONGUITUD; i++)
    {
    cout << lista[i] << " ";
}

    system("pause");
    return 0;
}

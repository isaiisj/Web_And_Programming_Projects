#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector <int> lista;
    
    int numero;
    
    cin >> numero;
    
    while(numero != -1)
    {
                 lista.push_back(numero);
                 cin >> numero;
    }
    
    int p;
    cout << "\n\nEl vector es:\n\n" << endl;
    for(p=0;p < lista.size(); p++)
              cout << lista[p] <<"";
    cout << "\n\n" << endl;
              
    system("pause");
    return o;
}

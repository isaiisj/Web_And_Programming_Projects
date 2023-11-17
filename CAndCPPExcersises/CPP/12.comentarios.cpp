#include<iostream>

using namespace std;
/*Esto es un comentario*/
int main() 
{
    char c;// un caracter 
    cout << "escribe una letra" << endl;
    cin >> c;
    switch(c)
    {
             case 'a':
             case 'e':
             case 'i':
             case 'o':
             case 'u':
                  cout << "Es una vocal" << endl;                    
                  break;
                  default:
                          cout << "Es una consonante" << endl;
                          }
                          system("pause");
                          return 0;
                          }

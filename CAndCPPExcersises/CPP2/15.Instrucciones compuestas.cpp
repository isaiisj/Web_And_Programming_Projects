#include<iostream>
using namespace std;

int main()
{
    if(5 < 8)
    {
         int a = 5 + 10;
         if(a > 12)
         {
              cout << a << endl;
         }
    }
    else
    {
        cout << "dentro del else" << endl;
        cout << "otra instruccion" << endl;
    }
    system("pause");
    return 0;
}

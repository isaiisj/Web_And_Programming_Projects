#include<iostream>
using namespace std;
int cubo (int);

int main()
{
    
    cout << " El resultado es: " << cubo (5) << endl;
    system("pause");
    return 0;
}
int cubo (int x)
{
    return(x * x * x);
}

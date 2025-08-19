#include <iostream>
#include <string>

class MinhaClassse 
{
    public:
    int n1, n2, n3;
    void calcular(int);
};
void MinhaClassse::calcular(int x = 1)
{
    n1 = 0;
    n2 = 1;
    std::cout<< n1 << " " << n2;
    for (int i = 1; 1<= x-2; i++) {
        n3 = n1 + n2;
        std::cout << " " << n3;
        n1 = n2;
        n2 = n3;
    }
}
int main()
{
    MinhaClassse objeto;
    objeto.calcular();
}
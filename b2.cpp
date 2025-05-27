#include <iostream>
using namespace std;
int main()
{
  int n = 154368;
  int sum = 0;
  while (n)
  {
    cout << (n % 10);
    sum = sum + n % 10;
    n = n / 10;
  }
  if (sum % 9 == 0)
    cout << ("\nTrue");
  else
    cout<<("\nFalse");
  return 0;
}
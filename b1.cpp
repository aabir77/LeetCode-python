#include <iostream>
using namespace std;

int main()
{
  int num, lastDigit, sum = 0;
  cin >> num;
  
  while (num != 0)
  {
    lastDigit = num % 10;  // 154368
    sum = sum + lastDigit; // 0 + 8..then we need next number
    num = num / 10;        // 15436
  }
  cout << sum << endl;

  if (sum % 9 == 0)
  {
    cout << "YES!";
  }
  else
    cout << "NOOO!";
  return 0;
}
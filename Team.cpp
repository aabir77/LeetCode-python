#include <iostream>
using namespace std;
int main()
{
  int n,count = 0,x, y, z;
  cin >> n;
  while (n--)
  {
    cin >> x >> y >> z;
    if (x == 1 && y == 1)
    {
      count++;
    }
    else if (y == 1 && z == 1)
    {
      count++;
    }
    else if (z == 1 && x == 1)
    {
      count++;
    }
    else{
    continue;
    }
  }
  cout<<count;
  return 0;
}
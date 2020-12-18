#include <iostream>
#include <iterator>
#include <string>
#include <sstream>
#include <vector>

int main()
{
  std::string str = "This is a string";

  std::istringstream buf(str);
  std::istream_iterator<std::string> beg(buf), end;
  std::vector<std::string> tokens(beg, end);

  for (const auto& i : tokens)
      std::cout << i << std::endl;

  return 0;
}

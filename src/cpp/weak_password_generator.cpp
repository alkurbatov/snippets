#include <iostream>
#include <stdlib.h>
#include <string>
#include <time.h>

int main()
{
    std::string symbols("abcdefghijklmnopqrstuvwxyz"
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        "1234567890"
                        "!@#$%^&*()`~-_=+[{]{\\|;:'\",<.>/?");

    srand(time(0)); //make it static if you need to call this gen function several time a row.

    for (size_t i = 0; i < 20; ++i)
    {
        //Add letter, capital letter, digit and symbol to satisfy Windows Password Policy
        std::string str("aA1?");

        while (str.length() < 20)
            str += symbols[rand() % symbols.length()];

        std::cout << str << std::endl;
    }

    return 0;
}

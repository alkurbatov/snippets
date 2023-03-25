#include <iostream>
#include <boost/nondet_random.hpp>
#include <boost/random/variate_generator.hpp>
#include <boost/random/uniform_int.hpp>

int main()
{
    std::string chars(
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "1234567890"
        "!@#$%^&*()"
        "`~-_=+[{]{\\|;:'\",<.>/?");

    boost::random_device rng;
    boost::variate_generator<boost::random_device&, boost::uniform_int<>>
        gen(rng, boost::uniform_int<>(0, chars.size()));

    for(size_t i = 0; i < 8; ++i)
        std::cout << chars[gen()];

    std::cout << std::endl;
    return 0;
}

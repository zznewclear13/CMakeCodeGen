#include "Bar.h"

#include <iostream>

Bar::Bar(IoCStack& ioc)
    :IDummy{}
{
}

void Bar::SayHello()
{
    std::cout << "Bar::SayHello" << std::endl;
}
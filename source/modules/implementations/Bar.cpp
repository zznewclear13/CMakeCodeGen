#include "Bar.h"

#include <iostream>

Bar::Bar(IoCStack& ioc)
    :IDummy{}
{
}

void Bar::SayHello() const
{
    std::cout << "Bar::SayHello" << std::endl;
}
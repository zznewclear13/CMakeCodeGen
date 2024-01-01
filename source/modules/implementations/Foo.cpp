#include "Foo.h"

#include <iostream>

Foo::Foo(IoCStack& ioc)
    :IDummy{}
{
}

void Foo::SayHello()
{
    std::cout << "Foo::SayHello" << std::endl;
}
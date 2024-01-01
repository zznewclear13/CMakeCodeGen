#pragma once

#include "ioc_system/IoCStack.h"
#include "api/IDummy.h"

class Foo : public IDummy
{
public:
    Foo(IoCStack& ioc);
    void SayHello() override;
};
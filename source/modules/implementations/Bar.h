#pragma once

#include "ioc_system/IoCStack.h"
#include "api/IDummy.h"

class Bar : public IDummy
{
public:
    Bar(IoCStack& ioc);
    void SayHello() override;
};
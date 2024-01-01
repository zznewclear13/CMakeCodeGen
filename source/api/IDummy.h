#pragma once

class IDummy
{
public:
    virtual ~IDummy() = default;
    virtual void SayHello() = 0;
};
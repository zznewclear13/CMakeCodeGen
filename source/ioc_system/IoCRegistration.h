#pragma once

#include <functional>

class IoCStack;

struct IoCRegistration
{
    using CTor = std::function<void(void*, IoCStack&)>;
    using DTor = std::function<void(void*)>;

    size_t objectSize{ 0 };
    CTor cTor{ nullptr };
    DTor dTor{ nullptr };
};

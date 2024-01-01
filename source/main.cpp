#include "module_system/ModuleManager.h"
#include "ioc_system/IOCStack.h"

#include "api/IDummy.h"

#include <iostream>

int main()
{
    std::cout << "CMake Code Generation Example." << std::endl;
    
    ModuleManager::RegisterAllModules();
    
    IoCStack stack{};
    stack.Get<IDummy>().SayHello();
    stack.Get<IDummy>("bar").SayHello();

    system("PAUSE");
    return 0;
}
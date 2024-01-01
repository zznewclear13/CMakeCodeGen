#include "module_system/ModuleManager.h"


#include "modules/dummy.bar.h"
#include "modules/dummy.foo.h"

void ModuleManager::RegisterAllModules()
{

    ModuleManager::Get().Register<dummy_bar>();
    ModuleManager::Get().Register<dummy_foo>();
    
}
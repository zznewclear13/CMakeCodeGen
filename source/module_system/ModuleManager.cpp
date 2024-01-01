#include "ModuleManager.h"

void ModuleManager::Register(std::unique_ptr<IModule>&& module)
{
    module->Register(IoCRegistrations::Get());
    m_modules[module->GetDesc().packageName] = std::move(module);
}

const ModuleDescription* ModuleManager::GetModuleDetail(const std::string& packageName) const
{
    auto it = m_modules.find(packageName);
    if (it != m_modules.end())
    {
        return &it->second->GetDesc();
    }
    return nullptr;
}

IModule* ModuleManager::GetModulePtr(size_t index) const
{
    auto it = m_modules.begin();
    for (size_t i = 0; i < index; i++) ++it;
    return it->second.get();
}

const ModuleDescription* ModuleManager::GetModuleDetail(size_t index) const
{
    auto it = m_modules.begin();
    for (size_t i = 0; i < index; i++) ++it;
    return &it->second->GetDesc();
}

size_t ModuleManager::GetModuleCount() const
{
    return m_modules.size();
}

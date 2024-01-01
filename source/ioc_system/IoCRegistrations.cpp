#include "ioc_system/IoCRegistrations.h"

IoCRegistrations& IoCRegistrations::Get()
{
    static IoCRegistrations instance;
    return instance;
}

const IoCRegistration* IoCRegistrations::Lookup(std::type_index type, std::string_view name) const
{
    const IoCRegistration* registration = nullptr;
    auto itType = m_registrations.find(type);
    if (itType != m_registrations.end())
    {
        const auto& map2 = itType->second;
        auto itName = map2.find(std::string(name));
        if (itName != map2.end())
        {
            registration = &itName->second;
        }
    }

    return registration;
}

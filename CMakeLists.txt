cmake_minimum_required(VERSION 3.20.0 FATAL_ERROR)

set(CMAKE_CODE_GEN_NAME "CMakeCodeGen")
message("[${CMAKE_CODE_GEN_NAME}] CMake configuration begins...")

project(
    "CMake Code Generation"
    DESCRIPTION "A code generation project using CMake, Python and Jinja2."
    LANGUAGES CXX
)

if(NOT MSVC)
    message(FATAL_ERROR "This app currently only supports MSVC for building." )
endif()
set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)

find_package(Python REQUIRED)
if(NOT Python_FOUND)
    message(FATAL_ERROR "Python not found." )
endif()

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CONFIGURATION_TYPES Debug Release)
set_property(DIRECTORY ${CMAKE_CODE_GEN_PROJECT_DIR} PROPERTY VS_STARTUP_PROJECT ${CMAKE_CODE_GEN_NAME})

set(CMAKE_CODE_GEN_PROJECT_DIR ${CMAKE_SOURCE_DIR})
set(CMAKE_CODE_GEN_SOURCE_DIR ${CMAKE_CODE_GEN_PROJECT_DIR}/source)
set(CMAKE_CODE_GEN_INCLUDE_DIR ${CMAKE_CODE_GEN_PROJECT_DIR}/include ${CMAKE_CODE_GEN_SOURCE_DIR})
set(CMAKE_CODE_GEN_LIBRARY_DIR ${CMAKE_CODE_GEN_PROJECT_DIR}/library)
set(CMAKE_CODE_GEN_BINARY_DIR ${CMAKE_CODE_GEN_PROJECT_DIR}/binary)
message("[${CMAKE_CODE_GEN_NAME}] PROJECT_DIR: ${CMAKE_CODE_GEN_PROJECT_DIR}")

foreach(config IN ITEMS ${CMAKE_CONFIGURATION_TYPES})
    string(TOUPPER ${config} CONFIG)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_${CONFIG} ${CMAKE_CODE_GEN_BINARY_DIR}/${config}/bin)
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_${CONFIG} ${CMAKE_CODE_GEN_BINARY_DIR}/${config}/dll)
    set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_${CONFIG} ${CMAKE_CODE_GEN_BINARY_DIR}/${config}/lib)
endforeach()

add_subdirectory("source")
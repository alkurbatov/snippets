cmake_minimum_required(VERSION 3.18)

project(Snippets)

# Specify output directories.
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

# Build with c++17 support.
set(CMAKE_CXX_STANDARD 17)

find_package(Boost 1.71.0 REQUIRED COMPONENTS random)
include_directories(${Boost_INCLUDE_DIRS})
link_directories(${Boost_LIBRARY_DIRS})

if (CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall \
        -Wno-c++98-compat -Wno-c++98-compat-pedantic -Wno-padded \
        -Wno-switch-enum -Wno-weak-vtables -Wno-exit-time-destructors \
        -Wno-float-equal -Wno-global-constructors"
    )
endif ()

set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG")

set(Solutions
    strong_password_generator
    tokenize
    weak_password_generator
)

foreach(solution IN LISTS Solutions)
    add_executable(${solution} ${solution}.cpp)
    target_link_libraries(${solution} boost_random-mt)
endforeach()

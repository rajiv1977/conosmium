# conosmium

# This branch provides a conan build for libosmium.
  - Template for builiding any map based projects.
  - Further infor for libosmim: https://github.com/osmcode/libosmium

# Prerequisite (Windows or Unix):
* Conan
* CMake

# Build (Window): 
  - not tested yet.

# Build (Unix):
```Matlab
conan install . -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True --output-folder=build --build=missing --settings=build_type=Debug
cd build
cmake .. -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE=./build/build/Debug/generators/conan_toolchain.cmake -DCMAKE_POLICY_DEFAULT_CMP0091=NEW -DCMAKE_BUILD_TYPE=Debug
cmake --build . --config Debug
./conosmium
```
# Testing:
  input file is in the data folder, put it in the build folder before running './conosmium'
import os

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan.tools.build import check_min_cppstd
from conan.errors import ConanInvalidConfiguration
from conan.tools.files import copy

class Conosmium(ConanFile):
    name = "conosmium"
    version = "1.0"
    
    author = "Rajiv Sithiravel"
    
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False], "optimized": [1, 2, 3]}
    default_options = {"shared": False, "fPIC": True, "optimized": 1}
    
    exports_sources = "CMakeLists.txt", "source/*", "include/*"
        
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
            
    def configure(self):
        if self.options.shared:
            del self.options.fPIC
            
    def validate(self):
        print(self.settings.os)
        if self.settings.os == "Windows":
            if self.settings.compiler == "msvc":
                check_min_cppstd(self, "20")
            elif self.settings.compiler == "intel-cc":
                check_min_cppstd(self, "gnu23")
                self.settings.compiler.mode = "dpcpp"      
                
    def validate(self):
        if self.settings.os == "Linux":
            if self.settings.compiler == "gcc":
                check_min_cppstd(self, "gnu23")
         
    status = 0;         
    def validate(self):
        if self.settings.os != "Windows":
            status = 1;
        elif self.settings.os != "Linux":
            status = 2;      
        if(status == 0):    
            raise ConanInvalidConfiguration("This package is only compatible with Windows or Linux")
                                                                    
    def requirements(self):
        self.requires("boost/1.86.0") 
        self.requires("expat/2.5.0")
        self.requires("gdal/3.8.3")
        self.requires("geos/3.12.0")
        self.requires("lz4/1.10.0")
        self.requires("protobuf/5.27.0")
        self.requires("utfcpp/4.0.5")     
        self.requires("zlib/1.3.1")
               
    def build_requirements(self):
        self.tool_requires("cmake/3.28.1")
               
    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()
 
    def layout(self):
        cmake_layout(self)
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()




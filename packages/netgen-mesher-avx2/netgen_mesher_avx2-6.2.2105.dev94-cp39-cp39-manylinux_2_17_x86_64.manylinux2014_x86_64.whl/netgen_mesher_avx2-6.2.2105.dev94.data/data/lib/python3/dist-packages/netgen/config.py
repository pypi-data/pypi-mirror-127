def _cmake_to_bool(s):
    return s.upper() not in ['', '0','FALSE','OFF','N','NO','IGNORE','NOTFOUND']

is_python_package    = _cmake_to_bool("TRUE")

BUILD_FOR_CONDA     = _cmake_to_bool("ON")
BUILD_STUB_FILES    = _cmake_to_bool("OFF")
CHECK_RANGE         = _cmake_to_bool("OFF")
DEBUG_LOG           = _cmake_to_bool("OFF")
ENABLE_CPP_CORE_GUIDELINES_CHECK  = _cmake_to_bool("OFF")
ENABLE_UNIT_TESTS   = _cmake_to_bool("OFF")
INSTALL_PROFILES    = _cmake_to_bool("OFF")
INTEL_MIC           = _cmake_to_bool("OFF")
TRACE_MEMORY        = _cmake_to_bool("OFF")
USE_CCACHE          = _cmake_to_bool("ON")
USE_CGNS            = _cmake_to_bool("OFF")
USE_GUI             = _cmake_to_bool("ON")
USE_INTERNAL_TCL    = _cmake_to_bool("ON")
USE_JPEG            = _cmake_to_bool("OFF")
USE_MPEG            = _cmake_to_bool("OFF")
USE_MPI             = _cmake_to_bool("OFF")
USE_MPI4PY          = _cmake_to_bool("ON")
USE_NATIVE_ARCH     = _cmake_to_bool("OFF")
USE_NUMA            = _cmake_to_bool("OFF")
USE_OCC             = _cmake_to_bool("ON")
USE_PYTHON          = _cmake_to_bool("ON")
USE_SPDLOG          = _cmake_to_bool("OFF")

CMAKE_INSTALL_PREFIX  = "/tmp/pip-req-build-8_85vcnl/_skbuild/linux-x86_64-3.9/cmake-install"
NG_INSTALL_DIR_PYTHON   = "lib/python3/dist-packages"
NG_INSTALL_DIR_BIN      = "bin"
NG_INSTALL_DIR_LIB      = "lib"
NG_INSTALL_DIR_INCLUDE  = "include"
NG_INSTALL_DIR_CMAKE    = "lib/cmake/netgen"
NG_INSTALL_DIR_RES      = "share"

NETGEN_PYTHON_RPATH_BIN = "../../../bin"
NETGEN_PYTHON_RPATH     = "netgen_mesher_avx2.libs"
NETGEN_PYTHON_PACKAGE_NAME = "netgen-mesher-avx2"

NG_COMPILE_FLAGS           = "-march=core-avx2"
ngcore_compile_options     = "-march=core-avx2"
ngcore_compile_definitions = "NETGEN_PYTHON;NG_PYTHON"

NETGEN_VERSION = "6.2.2105-94-gccf818b0"
NETGEN_VERSION_GIT = "v6.2.2105-94-gccf818b0"
NETGEN_VERSION_PYTHON = "6.2.2105.dev94"

NETGEN_VERSION_MAJOR = "6"
NETGEN_VERSION_MINOR = "2"
NETGEN_VERSION_TWEAK = "94"
NETGEN_VERSION_PATCH = "2105"
NETGEN_VERSION_HASH = "gccf818b0"

version = NETGEN_VERSION_GIT

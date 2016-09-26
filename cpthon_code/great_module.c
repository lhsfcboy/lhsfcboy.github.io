//great_module.c

//gcc -fPIC -shared -msse4.2 great_module.c -o great_module.dll
#include <nmmintrin.h>

#ifdef _MSC_VER
    #define DLL_EXPORT __declspec( dllexport ) 
    #else
        #define DLL_EXPORT
        #endif

        DLL_EXPORT int great_function(unsigned int n) {
            return _mm_popcnt_u32(n);
            }

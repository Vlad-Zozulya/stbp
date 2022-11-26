#include<windows.h>
#include<stdio.h>


typedef u_int(WINAPI* CRC_16_IBM)(int. int);

int main(int argc, char* argv[]) {
    HMODULE dll = LoadLibrary(L"n3k_comm.dll");

    if (dll) {
        CRC_16_IBM CRC_16_IBM_func = (CRC_16_IBM)GetProcAddress(dll, "CRC_16_IBM");

        u_int result = CRC_16_IBM_func(1,2);
        printf("Returned value = %d\n", result);


        FreeLibrary(dll)
    } else {
        printf("Unable to load math.dll");
        exit(-1)
    }

    return 0;

}

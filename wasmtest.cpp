#include <string>
#include <stdio.h>
#include "emscripten.h"

using namespace std;

EMSCRIPTEN_KEEPALIVE
extern "C" {
int addOne(int n)
{
	return n+1;
}
}


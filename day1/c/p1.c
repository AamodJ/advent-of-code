#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  FILE * fp = fopen("../input.txt", "r");
  if (fp == NULL) { 
    printf("Error opening file stream. Aborting");
    return -1;
  }

  char * line = NULL;
  size_t line_len = 0;

  char dir;
  char * mag = malloc(sizeof(char) * 8);
  long magnitude = 0;

  long pos = 50;
  long passwd = 0;

  long steps = 0;

  while (getline(&line, &line_len, fp) != -1) {
    steps++;
    dir = line[0]; 
    strncpy(mag, line + sizeof(char), sizeof(&line) - sizeof(char));
    magnitude = strtol(mag, NULL, 10);

    if (dir == 'L') {
      pos = pos - magnitude;
    }
    else {
      pos = pos + magnitude;
    }

    pos = (100 + pos) % 100;
    if (pos == 0) {
      passwd++;
    }
    // printf("Step: %ld. Direction: %c. Magnitude %ld. Position: %ld\n", steps, dir, magnitude, pos);
  }

  printf("Final position: %ld. Password: %ld\n", pos, passwd);

  fclose(fp);
  free(mag);
  free(line);

  return 0;
}

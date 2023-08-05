/// \file main.c
///
///
/// Notes on use with the CodeChat System
/// -------------------------------------
/// Compared to a standard `Doxyfile` Doxygen configuration file generated by `doxygen -g`, the `Doxyfile` in this project:
///
/// -  The `Doxyfile` setting for `OUTPUT_DIRECTORY` must (mostly) match the output directory of the CodeChat project configuration file `codechat_config.yaml`. With a `Doxyfile` parameter `OUTPUT_DIRECTORY` set to `_build`, the correct corresponding `codechat_config.yaml` setting for `output_path` is `_build/html`.
/// -   The `RECURSIVE` setting was changed to `YES`, since this seems like a more reasonable default.
///
/// To use these files, simply copy them to a new project directory of your choice. Open them in your preferred text editor/IDE, then use a appropriate CodeChat extension/plugin to open any of these files to build and view the results.

#include <stdio.h>

/// The main routine.
int main(int argc, char** argv) {
    printf("Hello, world!\n");
}
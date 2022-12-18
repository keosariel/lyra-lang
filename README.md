![lyra](/assets/art/header.png)
# Lyra Programming Language

**[lyralang.org](https://lyralang.org/)** | **[Wiki](https://github.com/mescalinsemi/lyra-lang/wiki)**

Lyra is a powerful and versatile programming language that combines the simplicity and expressiveness of Python3.12 and Perl5.10 with the power and efficiency of asynchronous programming and performance of LLVM. Its friendly and intuitive syntax makes it easy to learn and use, while its advanced compilation, subset and tools lead to mission assurance in various fields. Its design and optimization techniques allow it to tackle even the most demanding engineering tasks. With Lyra, you can design, synthesize, and manufacture CPUs, SoCs, and other microprocessors, as well build scalable and efficient operating systems, web and mobile apps, and more.

## Road Map

- [x] Lexer & Parser (AST)
- [x] Typechecker
- [ ] Primitives (int, float, struct, char, bools, functions)
- [ ] Pointers
- [ ] Dynamic memory allocation & deallocation
- [ ] External libraries
- [ ] LLVM code generator
- [ ] Filesystem
- [ ] Sockets
- [ ] Threads
- [ ] Unittests
- [ ] CLI

  ## Features
- **Fast and compiled**, With C/Julia comparable speed and LLVM's cutting-edge optimizations, Lyra eliminates the need for tedious performance tweaking on your end.

- **Statically typed** so you don't need to guess the type of the variable if your coworker didn't spend the time to use meaningful names and you can make use of compile-time checks, autocomplete and more

- **Simple and expressive** because the code should be easily readable and it shouldn't make you guess what it does, but you can give it your very personal touch and style


## How to run, compile or translate .ly files/projects

```
./lyra --compile <filename>
./lyra --generate-ast <filename>
./lyra --print-ast <filename>
./lyra --generate-llvm <filename>
./lyra --print-llvm <filename>
./lyra --generate-hdl <filename>
./lyra --help

```

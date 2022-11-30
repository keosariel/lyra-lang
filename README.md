# Lyra - A discreet, syntax liberal, llvm ahead-of-time optimized programming language 
## Useful for everything from Verilog gate level synthesis to High Level Web Apps and Mobile apps with NoSQL
## Defeating your Antivirus soon by default running in curve25519 encrypted memory!

![Lyra Lang](https://github.com/zdanl/lyra-lang/blob/main/github-header-image%20(1).png?raw=true)

This is a compiler for Lyra Language, built with Python 3.8+ (soon Python3.12+ once we get llvmlite to run) and the LLVM framework using the python3-llvmlite library. It supports C/C++ type multiline comments, single line comments of both C/C++ and Python typical syntax/standards, also JuliaLang features as to commentary, and this doesn't stop with there. Contrary to Python as to dynamic implementation of its class structure and inheritance system of Object/Function Prototypes similiary thought as v8 Javascript prototypes; due to the dynamic nature of the language running itself, quite different from Javascript v8 in that manner, it supports (will support) a Lexically inbound Compiled Class Token, which Julia lacks by parallel integration of them with structs and wiring of functions into the structs, to the best of our knowledge, meaning that as in Python "def" or "func, Perl "sub", will be equal oppertunity lexical tokens contesting "class" including its parameters, but *not* the Lyra typical precondition of a method to announce its return value type, as in func test():int. This is tricky to implement in the Lexer and Parser. The useit-for-anything-but-multi-platform-cross-architecture-malware language  is very punctuation liberal and allows different styles of addressing memory from data structures. For example the following are legitimate accessors for both object attributes and dictionary keys ´´ -> :: : . ´´ 

You may soon use indentation OR sharp braces, and you may use a semicolon whenever you like. 
 
 ## Features
- **it's fast**, because it should be so, together with LLVM's state of the art optimizations, but it won't ever oblige you to make
                 an extra effort from your side just for the sake of performance

- **it's compiled** using llvmlite

- **it's statically typed** so you don't need to guess the type of the variable if your coworker didn't spend the time to use meaningful names and you can make use of compile-time checks, autocomplete and more

- **it's simple and expressive** because the code should be easily readable and it shouldn't make you guess what it does, but you can give it your very personal touch and style

Install the requirements
```bash
pip3.8 install -r requirements.txt
```

# ./tests

> These are all working perfectly, a unittest like test runner is being built.

## ./lyra

This is the compiler.

It supports multiple features as in just printing the AST, generating LLVM IR, compiling statically before not running, or just running.

The language was inspired by the originally forked Github repository type-wise, and clearly a mix of Python3 and Perl5.10 syntax wise.

```
def fact(n:int):int{
    if n <= 1{
        return 1
    }
    return n * fact(n-1)
}

def main():int{
    return fact(6)
}
```

## Conditionals

```
def main():int{

    age = 18
    if age == 18{
        printf('wow you are 18\n')
    }else{
        printf('i guess you are not 18\n')
    }

    return 0
}
```

## Loops

```
def main():int{

    printf('while loop\n')
    x = 0
    while x < 10{
        printf('x = %i\n',x)
        x = x+1
    }

    printf('Until loop\n')

    x = 0
    until x > 10{
        printf('x = %i\n',x)
        x = x+1
    }

    return 0
}
```
## How to run it

```
./lyra --compile <filename>
```

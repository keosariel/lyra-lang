# Lyra Programming Language

Lyra is a powerful and versatile programming language that combines the simplicity and expressiveness of Python3.12 and Perl5.10 with the power and efficiency of asynchronous programming and performance of LLVM. Its friendly and intuitive syntax makes it easy to learn and use, while its advanced compilation, subset and tools guide for mission assurance in various fields. Its design and optimization techniques allow it to tackle even the most demanding engineering tasks. With Lyra, you can design, synthesize, and manufacture CPUs, SoCs, and other microprocessors, as well build scalable and efficient operating systems, web and mobile apps, and more.
This is the official description and, so far, documentation website.

## Road Map
https://mescalin.notion.site/Lyra-Roadmap-2023-ca9fd5822b9449b39461ef03f0c72c49

| Predicted Version | Description of Progress | Timestamp |
| --------------- | --------------- | --------------- |
| Original | Type system, functional language, Lexer/Compiler | This was the original work |
| 0.2 | Multiline comments and different styles of it are working | 30/11/2022 |
| 0.2 | Implementing support for OOP is in Progress | 30/11/2022 |
| 0.3 | Support for system calls like files  | 05/12/2022 |
| 0.3 | Support for system calls like sockets  | 15/12/2022 |
| 0.4 | And so on  | 20/12/2022 |

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

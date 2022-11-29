# Lyra - A discreet, syntax leftist, llvm ahead-of-time optimized, privacy, programming language 
## Defeating your Antivirus soon by default!

![Lyra Lang](https://github.com/zdanl/lyra-lang/blob/main/github-header-image%20(1).png?raw=true)

This is a compiler for Lyra Language, built with Python 3.8+ and the LLVM framework using the llvmlite library. It supports C/C++ type multiline comments, single line comments, as well as Python typical syntax and Julia Lang features as to commentary. Contrary to Python as to dynamic implementation it supports a Lexically inbound Compiled Class system, which Julia lacks by parallel integration with structs and wiring of functions, to the best of our knowledge. It is very punctuation liberal and allows different styles of addressing memory from data structures. For example the following are legitimate accessors for both object attributes and dictionary keys ´´ -> :: : . ´´ 
 
 ## Features
- **it's fast**, because it should be so, together with LLVM's state of the art optimizations, but it won't ever oblige you to make
                 an extra effort from your side just for the sake of performance

- **it's compiled** using llvmlite

- **it's statically typed** so you don't need to guess the type of the variable if your coworker didn't spend the time to use meaningful names and you can make use of compile-time checks, autocomplete and more

- **it's simple and expressive** because the code should be easily readable and it shouldn't make you guess what it does

Install the requirements
```bash
pip install -r requirements.txt
```

# Code examples

> These are all working perfectly

## Factorial Function

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
python run.py <filename>
```

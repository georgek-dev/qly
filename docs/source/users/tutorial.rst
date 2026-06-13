==================================
Getting Started with quickly / qly
==================================

Welcome to qly!
===============
qly (short for quickly) is a quick, interpreted language. You can use it for quite a lot of stuff and its syntax may seem crazy at the start but with time it will feel way easier :)

Um, but what even is a programming language?
--------------------------------------------
Imagine as if you could control computers by using a language to talk to them. The concept of programming languages is exactly this - allowing you to write instructions (known as: **code**) that help you to control your computer. In fact, all programming languages convert their code to a language named "Assembler". But it is very hard to type and read and it also varies by computer architecture. Take this code that prints "1234" on the screen in ARM64 assembler:

.. code-block:: asm
    .global _main
    .align 4
    
    .text
    _main:
        mov x0, #1          
        adrp x1, message@PAGE 
        add x1, x1, message@PAGEOFF 
        mov x2, #5         
        mov x16, #4        
        svc #0x80         

        mov x0, #0       
        mov x16, #1     
        svc #0x80      

    .data
    message:
        .ascii "1234\n"

Whereas in qly it's just:
.. code-block
    val .text int 1234
    ln .text

Some programming languages make it even shorter. For example, in Python you'd type:

.. code-block:: python
    print(1234)

And some are longer. Take C for example:

.. code-block:: C
    #include <stdio.h>

    int main() {
        printf("1234");
        return 0;
    }

All programming languages have their pros and cons.

And what's an interpreted programming language?
-------------------------------------------------
Interpreted programming languages are 

Your first program
==================
Now, make sure that you can run "qly" from your terminal. Save the following code in "test.qls":
.. code-block
    val .hello int 1
Now, run in your terminal: "qly test.qls". If everything goes well, you will see no output. But why's that? Because we are not outputting anything. However something has happened: the program has stored your text 1 in a variable with the name "hello". Now if we leave the . in front of hello away, 

==================================
Getting Started with quickly / qly
==================================

Welcome to qly!
===============
qly (short for quickly) is a quick, interpreted language. You can use it for quite a lot of stuff and its syntax may seem crazy at the start but with time it will feel way easier :)

Um, but what even is a programming language?
--------------------------------------------
Imagine as if you could control computers by using a language to talk to them. The concept of programming languages is exactly this - allowing you to write instructions (known as: **code**) that help you to control your computer. In fact, all programming languages convert their code to a language named "Assembler". But it is very hard to type and read and it also varies by computer architecture. Take this code that prints "1234" on the screen in ARM64 assembler:

.. code-block:: gas

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

.. code-block:: text

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

.. code-block:: text

    val .hello_world str "Hello, world!"

Now, run in your terminal: "qly test.qls". If everything goes well, you will see no output. But why's that? Because we are not outputting anything. However something has happened: the program has stored your text 1 in a variable with the name "hello". Now if we leave the . in front of hello away, the interpreter produces an error.
It outputs the following message:

.. code-block:: text

    error E003: variable name hello_world does not begin with a .

The message explains that a . needs to be in front of the variable name hello. Such messages can be helpful for debugging when your code doesn't work, so be sure to check your code once in a while.
Now, let's make the code do something. Add:

.. code-block:: text

    ln .hello_world

Your code should so look like this:

.. code-block:: text

    val .hello_world str "Hello, world!"
    ln .hello_world

Now, run the code. Let's retype "qly test.qls".

.. code-block:: text

    Hello, world!

That's all? Yes, because we only told the compiler to run that. Now try and change the "1" to your favorite number. Save and rerun. Now the output should be your favorite number.
But what happened exactly?

.. code-block:: text

    val .hello_world str "Hello, world!"

Here we told the program to create and store a variable with the name "hello" with a string value of "Hello, world!". However we can also save booleans instead! Just change "str" to "bool" and the text to "true" or "false" and rerun the code. qly also supports numbers, just make sure to change the type to int and the value to str.
And this line

.. code-block:: text

    ln .hello_world

tells the interpreter to output a line with the variable "hello".
Congratulations, you just wrote your first qly program!
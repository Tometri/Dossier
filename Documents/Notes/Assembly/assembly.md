# Assembly
## Modern Assembly Applications
Assembly is a low level programming language used to translate instructions from a higher level language (such as python) directly to binary. 
Example: Coding in python -> python to assembly -> assembly to binary.
Assembly has a few specific use cases throughout the industry: embedded systems that have limited memory and hardware capacity, direct hardware testing, software optimization.
Embedded systems and their micro-controllers are often programmed in assembly because it gives programmers control over hardware functions on a task by task level, ensuring the size and speed of the program maximizes hardware limits.
Certain algorithms can be optimized based on data storage and memory access techniques. Understanding how hardware implements these techniques can help a programmer develop superior code.
CodeAcademy: "There are several Assembly languages, each written for a specific processor, or more precisely, in accordance with a processor’s Instruction Set Architecture. Three primary industry competitors are the x86, ARM, and MIPS architectures, which account for the majority of desktop, mobile, and embedded technologies respectively."

## Compilation Process

In general there are four steps known as the compilation process which compose the journey high-level code goes on before reaching the hardware:

- Pre-processing: The first step of compilation. It is used to prepare the user's code for machine code by removing comments, expanding included macros, and performing any code maintenance prior to handing the file to the compiler.
- Compiling: The process of taking the expanded file from the preprocessor and translating the program into an optimized assembly language.
- Assembling: The process of taking an assembly language program and using an assembler to generate machine code.
- Linking: The process of filling in function calls, including additional objects, libraries, and source code from other locations into the main source code.

CodeAcademy: "While the compilation process is tailored to each language and architecture, the overall procedure is fairly standard. It is in the compiling and assembling stages where Assembly is generated and used to create machine code."

## Assembly Code Format

Assembly language and binary code have an almost direct translation between their outputs.
CodeAcademy:"Assembly was created as a mnemonic language to make machine code easier to read and write, one instruction translating to one instruction. In fact, most ISAs will have both the binary code and Assembly language breakdown on the same page when talking about specific instructions. "
Assembly, like binary, begins with an opcode.
Ex: Multiply function = MULT $3, $2.
In most Assembly instructions, what follows the opcodes are the memory locations to be operated on. These memory locations are referred to as operands. Generally, these are direct register addresses but can also be memory references to values stored in other types of memory such as the cache or RAM. 

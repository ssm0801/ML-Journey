## Program

Program is sequence of instruction written in some programming language
- Google Chrome
- MS Word
- File Explorer

## Process

Process is simply an _**instance of a program**_ that is being executed. Each process has a unique process ID (PID) assigned when it is launched.

Process works along with OS and requires various computer resources. 

- Code Segment: Contains the program code required to run the process.
- Data Segment: Contains global and static variables accessible throughout the program.
- Heap Memory: Used for dynamic memory allocation during execution.
- Stack: Stores local variables and function call information.
- Registers: Small memory locations used to store temporary variables and logic for short periods.

Each process has its own separate memory space, which prevents one process from corrupting another. However, because each process has separate memory, switching between processes can increase execution time.


## Thread

Thread is a unit of execution within process. Each Thread hash its own stack and registers but shares code, data and heap segments

- Single Threaded Process : only one thread executing
- Multi Threaded Process : multiple thread execute concurrently within same process

## Example

- MS Paint : is a program
- MS Paint is launched : its a process, with PID
- Creating rectangle in MS Paint (any other operation) : its a thread
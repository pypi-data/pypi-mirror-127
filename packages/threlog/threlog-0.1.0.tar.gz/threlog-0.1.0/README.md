# threlog
___

## Description
Simple multithreading logger.

## Installation
You have to use Python3.7 or latest version.
```shell
/your/project/path$ git clone https://github.com/RostovtsevDanila/threlog
```

## Usage
```python
from threlog import Logger
from multiprocessing.dummy import Process, Queue, Manager
from queue import Empty

def worker(q: Queue, l: Logger):
    while not q.empty():
        try:
            val = q.get(block=True)
            l.inf(f"Some info: {val}")
            l.dbg(f"Some debug: {val}")
            l.err(f"Some error: {val}")
        except Empty:
            continue
        

if __name__ == '__main__':
    with Logger(
        file="log_file_path.log",
        stdout_mode=(Logger.DEBUG, Logger.ERROR),
        file_mod=(Logger.INFO, Logger.ERROR)
    ) as logger:
        queue = Manager().Queue()
        threads = [Process(target=worker, args=(queue, logger, )) for _ in range(10)]
        [t.start() for t in threads]
        [t.join() for t in threads]
        
```
By this example DEBUG and ERROR logs will be printed to stdout, INFO and ERROR logs will be written to file.  

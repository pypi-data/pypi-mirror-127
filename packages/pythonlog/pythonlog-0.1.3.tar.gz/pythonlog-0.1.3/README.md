# pylog pypi-aka:pythonlog
The new python logger
## Install
`pip install pythonlog`
## How to use
### log
```
generates a log message

example:
    script:
        import pylog
        pylog.log("system.log","this is a log")
    output:
        [LOG] [0000-00-00 00:00:00.000000] this is a log
Args:
    location ([str]): [Defines the location of the log file]
    msg ([str]): [Message to log]
    log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
    file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
```
### debug
```
generates a debug log

example:
    script:
        import pylog
        pylog.debug("system.log","this is a log")
    output:
        [DEBUG] [0000-00-00 00:00:00.000000] this is a log
Args:
    location ([str]): [Defines the location of the log file]
    msg ([str]): [Message to log]
    log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
    file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
```
### warn
```
generates a warn log

example:
    script:
        import pylog
        pylog.warn("system.log","this is a log")
    output:
        [WARNING] [0000-00-00 00:00:00.000000] this is a log
Args:
    location ([str]): [Defines the location of the log file]
    msg ([str]): [Message to log]
    log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
    file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
```
### error
```
generates a error log

example:
    script:
        import pylog
        pylog.error("system.log","this is a log")
    output:
        [ERROR] [0000-00-00 00:00:00.000000] this is a log
Args:
    location ([str]): [Defines the location of the log file]
    msg ([str]): [Message to log]
    log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
    file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
```
### critical error
```
generates a critical error log

example:
    script:
        import pylog
        pylog.cerror("system.log","this is a log")
    output:
        [CRITICAL_ERROR] [0000-00-00 00:00:00.000000] this is a log
Args:
    location ([str]): [Defines the location of the log file]
    msg ([str]): [Message to log]
    log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
    file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
```
### fatal error
```
generates a critical error log

example:
    script:
        import pylog
        pylog.ferror("system.log","this is a log")
    output:
        [FATAL_ERROR] [0000-00-00 00:00:00.000000] this is a log
Args:
    location ([str]): [Defines the location of the log file]
    msg ([str]): [Message to log]
    log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
    file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
```
### messsage
```
writes a message in a log file

example:
    script:
        import pylog
        pylog.message("system.log","this is a log")
    output:
        this is a message
Args:
    location ([str]): [Defines the location of the log file]
    msg ([str]): [Message to log]
```
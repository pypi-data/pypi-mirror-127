# TheLogger

Easy to use logger object for creating code logs. Just import it and it's set up, ready to go.

### Installation

```
$ pip install thelogger
```

### Usage

my_script.py:
```python class:"lineNo"
from thelogger import lg

# log messages
lg.info('Hello World')
lg.warning('warning message')
lg.error('error message')

# start logging messages to a file
lg.reset(file = './demo_log.txt')

# shorthand convenience methods for logging messages
lg.i('this is an info message')
lg.w('this is a warning message')

# remove log handlers
lg.close()
lg.i('nothing is logged because there are no log handlers')

# add default log handlers
lg.reset()
```

Output to console:
```
[I 2021-11-13 08:50:36] Hello World
[W 2021-11-13 08:50:36] warning message
[E 2021-11-13 08:50:36] error message
[I 2021-11-13 08:50:36] this is an info message
[W 2021-11-13 08:50:36] this is a warning message
```

Output to demo_log.txt:
```
[I 2021-11-13 08:50:36 my_script:12] this is an info message
[W 2021-11-13 08:50:36 my_script:13] this is a warning message
```

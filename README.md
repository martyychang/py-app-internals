This project simply contains scripts and code snippets to show how to set up
a Python 2 app's basic components, such as logging.

## Logger demo

Every app should have an `app.internals` module which defines the `logger()`
function. The `logger()` function simply returns a `Logger` object, while the 
module takes care of configuring logging consistently for the whole app.

`logging.basicConfig()` is called once and only once in the `app.internals`
module, and the `logger()` method is for convenience, to save developers
from having to import both `app.internals` _and_ `logging` in other modules.

```bash
# To see how app.internals works
python src/logger.demo.py
```

## Tornado demo

Tornado is a web framework which can be used to build an API, with
support for `logging` all around.

```bash
# You'll be notified that the Tornado party is about to start...
python src/tornado.demo.py

# In a separate session or client, make a request to Tornado to see more
# loggers in action.
curl http://localhost:8888
```

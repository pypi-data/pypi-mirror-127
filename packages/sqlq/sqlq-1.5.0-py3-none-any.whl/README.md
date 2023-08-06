# Sqlite3 Execution Queue

<badges>[![version](https://img.shields.io/pypi/v/sqlq.svg)](https://pypi.org/project/sqlq/)
[![license](https://img.shields.io/pypi/l/sqlq.svg)](https://pypi.org/project/sqlq/)
[![pyversions](https://img.shields.io/pypi/pyversions/sqlq.svg)](https://pypi.org/project/sqlq/)  
[![powered](https://img.shields.io/badge/Say-Thanks-ddddff.svg)](https://saythanks.io/to/foxe6)
[![donate](https://img.shields.io/badge/Donate-Paypal-0070ba.svg)](https://paypal.me/foxe6)
[![made](https://img.shields.io/badge/Made%20with-PyCharm-red.svg)](https://paypal.me/foxe6)
</badges>

<i>A thread safe queue worker that executes SQL for multi-threaded applications.</i>

# Hierarchy

```
sqlqueue
|---- SqlQueueU()
|   |---- sql()
|   |---- _sql()
|   |---- sql_async()
|   |---- _sql_async()
|   |---- backup()
|   |---- commit()
|   '---- stop()
'---- SqlQueueE()
    |---- sql()
    |---- _sql()
    |---- sql_async()
    |---- _sql_async()
    |---- backup()
    |---- commit()
    '---- stop()
```

# Example

## python
See `test`.
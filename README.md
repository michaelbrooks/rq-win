Windows RQ Worker
======

Provides a WindowsWorker class that allows you to use
[Redis Queue (RQ)](https://github.com/nvie/rq) on Windows systems.
This is for development/testing purposes only.

Since Windows does not support fork(), we execute all work in the main
worker thread instead of forking off a separate worker process.
As a result, workers may not be as stable and crash resistant.

Further, since Windows does not support SIGALRM, WindowsWorkers
do not provide any of the work timeout controls that normal workers provide.

Installation and Use
-----------

You can install this package directly from GitHub with pip:

```bash
$ pip -e git+https://github.com/michaelbrooks/rq-win.git#egg=rq-win
```

To start an RQ worker using the WindowsWorker class:

```bash
$ rqworker -w rq_win.WindowsWorker
```

Contributions and improvements are welcome!

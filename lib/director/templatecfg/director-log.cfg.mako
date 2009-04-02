[loggers]
keys=root

[handlers]
keys=default

[formatters]
keys=default


[logger_root]
level=NOTSET
handlers=default
qualname=(root)
propagate=1
channel=
parent=

[handler_default]
class=handlers.RotatingFileHandler
args=("${log_dir}/director.log", "au", 10 * 1024 * 1024, 2)
level=DEBUG
formatter=default


[formatter_default]
format=%(asctime)s %(name)s %(levelname)s %(message)s
datefmt=
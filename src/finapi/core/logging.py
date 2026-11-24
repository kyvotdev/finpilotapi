import logging
import logging.config


def setup_logging() -> None:
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": (
                        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
                    ),
                    "datefmt": "%Y-%m-%d %H:%M:%S",
                },
                "access": {
                    "()": "uvicorn.logging.AccessFormatter",
                    "fmt": (
                        "%(asctime)s | "
                        "%(levelname)-8s | "
                        "%(client_addr)s | "
                        "%(request_line)s | "
                        "%(status_code)s"
                    ),
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "level": "DEBUG",
                    "formatter": "default",
                },
                "access_console": {
                    "class": "logging.StreamHandler",
                    "level": "INFO",
                    "formatter": "access",
                },
            },
            "loggers": {
                "my_api": {
                    "level": "DEBUG",
                    "handlers": ["console"],
                    "propagate": False,
                },
                "uvicorn": {
                    "level": "INFO",
                    "handlers": ["console"],
                    "propagate": False,
                },
                "uvicorn.error": {
                    "level": "INFO",
                    "handlers": ["console"],
                    "propagate": False,
                },
                "uvicorn.access": {
                    "level": "INFO",
                    "handlers": ["access_console"],
                    "propagate": False,
                },
                "sqlalchemy.engine": {
                    "level": "WARNING",
                    "handlers": ["console"],
                    "propagate": False,
                },
            },
            "root": {
                "level": "INFO",
                "handlers": ["console"],
            },
        }
    )

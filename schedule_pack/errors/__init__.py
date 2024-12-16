"""Классы ошибок пакета Расписание.

ErrorMessageEnum: Перечисление сообщений об ошибках приложения.

ErrorTemplateEnum: Перечисление шаблонов сообщений об ошибках приложения.

ScheduleError: Общая ошибка пакета Расписание.

ScheduleArgumentError: Ошибка некорректного параметра при инициализации расписания.

ScheduleItemError: Ошибка некорректного параметра инициализации элемента расписания.

TaskArgumentError: Ошибка некорректного параметра инициализации задачи.

"""

from schedule_pack.errors.schedule_error import (
    ScheduleError,
    ScheduleArgumentError,
    ScheduleItemError,
    TaskArgumentError,
)
from schedule_pack.errors.error_message_enum import ErrorMessageEnum
from schedule_pack.errors.error_template_enum import ErrorTemplateEnum


__all__ = [
    "ErrorMessageEnum",
    "ErrorTemplateEnum",
    "ScheduleError",
    "ScheduleArgumentError",
    "ScheduleItemError",
    "TaskArgumentError",
]

class ScheduleError(Exception):
    """Общая ошибка пакета Расписание.
    Attributes:
        message -- Сообщение об ошибке.
    """

    def __init__(self, message):
        super().__init__(message)


class ScheduleItemError(ScheduleError):
    """Ошибка некорректного параметра инициализации элемента расписания.
    Attributes:
        message -- Сообщение об ошибке.
    """

    def __init__(self, message):
        super().__init__(message)


class ScheduleArgumentError(ScheduleError):
    """Ошибка некорректного параметра при инициализации расписания.
    Attributes:
        message -- Сообщение об ошибке.
    """

    def __init__(self, message):
        super().__init__(message)


class TaskArgumentError(ScheduleError):
    """Ошибка некорректного параметра инициализации задачи.
    Attributes:
        message -- Сообщение об ошибке.
    """

    def __init__(self, message):
        super().__init__(message)

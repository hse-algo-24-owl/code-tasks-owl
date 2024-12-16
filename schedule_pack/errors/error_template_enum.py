from strenum import StrEnum


class ErrorTemplateEnum(StrEnum):
    """Перечисление шаблонов сообщений об ошибках приложения."""

    ERR_NOT_NUMBER_DUR_TEMPL = "Продолжительность этапа {0} не является числом"
    ERR_NEG_NUMBER_DUR_TEMPL = "Продолжительность этапа {0} меньше или равна нулю"
    ERR_INVALID_TASK_TEMPL = "Некорректный формат задачи на позиции [{0}] в списке задач для составления расписания"
    ERR_INVALID_STAGE_CNT_TEMPL = (
        "Количество этапов для задачи на позиции [{0}] не равно двум"
    )

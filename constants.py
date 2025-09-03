from typing import Literal

STATUS = Literal["!completed", "in progress", "completed"]
PRIORITY = Literal["low", "medium", "high"]

DEFAULT_STATUS: STATUS = "!completed"
DEFAULT_PRIORITY: PRIORITY = "low"

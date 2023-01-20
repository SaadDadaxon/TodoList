class TASK:
    class STATUS:
        CONSTANTS = (
            (0, "Todo"),
            (1, "In Process"),
            (2, "Done"),
            (3, "Cancelled"),
            )
        DEFAULT = 0

    class PRIORITY:
        CONSTANTS = (
            (0, "lowes"),
            (1, "low"),
            (2, "Middle"),
            (3, "High"),
            (4, "Highest"),
            )
        DEFAULT = 2

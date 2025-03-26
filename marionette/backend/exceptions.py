class InitializationErr(Exception):
    """Go ahead, take a wild guess on when this error is raised

       Spoiler: for when the app eats shit when initializing
    """

    def __init__(self, message="App unable to initialize", *args: object) -> None:
        super().__init__(*args)
        self.message = message

    def __str__(self) -> str:
        return self.message


class InvalidJSONFormat(Exception):
    """c'mon dipshit, i believe in you!!! when is this raised?

       Spoiler: when theres a post thing that has invalid JSON format (i rly believed in you that time..... Why do i even try...)
    """

    def __init__(self, message="somewhere™, something™ does not have a valid JSON format", *args: object) -> None:
        super().__init__(*args)
        self.message = message

    def __str__(self) -> str:
        return self.message


class LimitError(Exception):
    """okay yeah this one is kinda confusing,
       For error in limiting max number of cpu cores or amount of memory allocated (or both!! por que no los dos tyshii!!!)
    """

    def __init__(self, message="Error in limiting cpu or memroy usage", *args: object) -> None:
        super().__init__(*args)
        self.message = message

    def __str__(self) -> str:
        return self.message
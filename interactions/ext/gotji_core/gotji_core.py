from interactions import Client, Extension
from typing import Optional


class ExtensionName(Extension):

    def __init__(self, client: Client, *args, **kwargs):

        pass


def setup(client: Client, *args, **kwargs) -> Optional[Extension]:

    return ExtensionName(client, *args, **kwargs)

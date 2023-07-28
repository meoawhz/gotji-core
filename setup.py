from interactions.ext import Base, build, Version, VersionAuthor

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

data = {
    "name": "gotji_core",
    "description": "connect to Meoaw API",
    "long_description": long_description,
    "version": Version(
        version="1.0.1",
        author=VersionAuthor(name="meoawhz", email="meoaw.acc@gmail.com"),
    ),
    "link": "https://github.com/meoawhz/new.cord",
}


class MyThirdParty(Base):
    def __init__(self):
        super().__init__(**data)


library = MyThirdParty()
build(library)

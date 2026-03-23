GREETING: str = "PyStego {{VERSION}}, Copyright (c) 2026 Doug Zwick"
VERSION_MAJOR: int = 0
VERSION_MINOR: int = 0
VERSION_PATCH: int = 0
VERSION_BUILD: int = 0


def get_version_str() -> str:
  return f"v{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH} b{VERSION_BUILD}"


def get_greeting_str() -> str:
  return GREETING.replace("{{VERSION}}", get_version_str())


def main() -> None:
  print(get_greeting_str())


main()

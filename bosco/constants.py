"""Define constants with dataclasses for use in bosco."""

from dataclasses import dataclass


# chasten constant
@dataclass(frozen=True)
class Bosco:
    """Define the Bosco dataclass for constant(s)."""

    Application_Name: str
    Application_Author: str
    Emoji: str
    Name: str
    Programming_Language: str
    Separator: str
    Tagline: str
    Theme_Background: str
    Theme_Colors: str
    Website: str


bosco = Bosco(
    Application_Name="bosco",
    Application_Author="BoscoTeam",
    Emoji=":dizzy:",
    Name="bosco",
    Programming_Language="python",
    Separator="/",
    Tagline="bosco: Measure the performance of Python functions!",
    Theme_Background="default",
    Theme_Colors="ansi_dark",
    Website=":link: GitHub: https://github.com/gkapfham/chasten",
)


# humanreadable constant
@dataclass(frozen=True)
class Humanreadable:
    """Define the Humanreadable dataclass for constant(s)."""

    Yes: str
    No: str


humanreadable = Humanreadable(Yes="Yes", No="No")


# logger constant
@dataclass(frozen=True)
class Logger:
    """Define the Logger dataclass for constant(s)."""

    Function_Prefix: str
    Richlog: str
    Syslog: str


logger = Logger(
    Function_Prefix="configure_logging_",
    Richlog="chasten-richlog",
    Syslog="chasten-syslog",
)


# logging constant
@dataclass(frozen=True)
class Logging:
    """Define the Logging dataclass for constant(s)."""

    Debug: str
    Info: str
    Warning: str
    Error: str
    Critical: str
    Console_Logging_Destination: str
    Syslog_Logging_Destination: str
    Default_Logging_Destination: str
    Default_Logging_Level: str
    Format: str
    Rich: str


logging = Logging(
    Debug="DEBUG",
    Info="INFO",
    Warning="WARNING",
    Error="ERROR",
    Critical="CRITICAL",
    Console_Logging_Destination="CONSOLE",
    Syslog_Logging_Destination="syslog",
    Default_Logging_Destination="console",
    Default_Logging_Level="ERROR",
    Format="%(message)s",
    Rich="Rich",
)


# markers constant
@dataclass(frozen=True)
class Markers:
    """Define the Markers dataclass for constant(s)."""

    Bad_Fifteen: str
    Bad_Zero_Zero: str
    Code_Context: int
    Comma_Space: str
    Empty_Bytes: bytes
    Empty_String: str
    Ellipse: str
    Forward_Slash: str
    Dot: str
    Hidden: str
    Indent: str
    Newline: str
    Non_Zero_Exit: int
    Nothing: str
    Single_Quote: str
    Slice_One: int
    Small_Bullet_Unicode: str
    Space: str
    Tab: str
    Underscore: str
    Xml: str
    Zero: int
    Zero_Exit: int
    Percent_Multiplier: int


markers = Markers(
    Bad_Fifteen="<15>",
    Bad_Zero_Zero="",
    Code_Context=5,
    Comma_Space=", ",
    Empty_Bytes=b"",
    Empty_String="",
    Ellipse="...",
    Forward_Slash="/",
    Dot=".",
    Hidden=".",
    Indent="   ",
    Newline="\n",
    Non_Zero_Exit=1,
    Nothing="",
    Single_Quote="'",
    Slice_One=1,
    Small_Bullet_Unicode="\u2022",
    Space=" ",
    Tab="\t",
    Underscore="_",
    Xml="xml",
    Zero=0,
    Zero_Exit=0,
    Percent_Multiplier=100,
)

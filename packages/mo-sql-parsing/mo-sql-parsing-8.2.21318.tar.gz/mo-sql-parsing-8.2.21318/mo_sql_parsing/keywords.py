# encoding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Contact: Kyle Lahnakoski (kyle@lahnakoski.com)
#

# SQL CONSTANTS
from mo_parsing import *
from mo_parsing.infix import delimited_list

from mo_sql_parsing.utils import (
    SQL_NULL,
    int_num,
    to_json_call,
    ansi_string,
    ansi_ident,
    keyword,
)

NULL = keyword("null") / (lambda: SQL_NULL)
TRUE = keyword("true") / (lambda: True)
FALSE = keyword("false") / (lambda: False)
NOCASE = keyword("nocase")
ASC = keyword("asc")
DESC = keyword("desc")

# SIMPLE KEYWORDS
AS = keyword("as").suppress()
ALL = keyword("all")
BY = keyword("by").suppress()
CAST = keyword("cast")
CONSTRAINT = keyword("constraint").suppress()
CREATE = keyword("create").suppress()
CROSS = keyword("cross")
DISTINCT = keyword("distinct")
EXCEPT = keyword("except")
FROM = keyword("from").suppress()
FULL = keyword("full")
GROUP = keyword("group").suppress()
HAVING = keyword("having").suppress()
INNER = keyword("inner")
INTERVAL = keyword("interval")
JOIN = keyword("join")
LEFT = keyword("left")
LIKE = keyword("like")
LIMIT = keyword("limit").suppress()
MINUS = keyword("minus")
OFFSET = keyword("offset").suppress()
ON = keyword("on").suppress()
ORDER = keyword("order").suppress()
OUTER = keyword("outer")
OVER = keyword("over").suppress()
PARTITION = keyword("partition").suppress()
# PERCENT = keyword("percent").suppress()
RIGHT = keyword("right")
RLIKE = keyword("rlike")
SELECT = keyword("select").suppress()
TABLE = keyword("table").suppress()
THEN = keyword("then").suppress()
TOP = keyword("top").suppress()
UNION = keyword("union")
INTERSECT = keyword("intersect")
USING = keyword("using").suppress()
WHEN = keyword("when").suppress()
WHERE = keyword("where").suppress()
WITH = keyword("with").suppress()
WITHIN = keyword("within").suppress()
PRIMARY = keyword("primary").suppress()
FOREIGN = keyword("foreign").suppress()
KEY = keyword("key").suppress()
UNIQUE = keyword("unique").suppress()
INDEX = keyword("index").suppress()
REFERENCES = keyword("references").suppress()
RECURSIVE = keyword("recursive").suppress()
VALUES = keyword("values").suppress()

PRIMARY_KEY = Group(PRIMARY + KEY).set_parser_name("primary_key")
FOREIGN_KEY = Group(FOREIGN + KEY).set_parser_name("foreign_key")

# SIMPLE OPERATORS
CONCAT = Literal("||").set_parser_name("concat")
MUL = Literal("*").set_parser_name("mul")
DIV = Literal("/").set_parser_name("div")
MOD = Literal("%").set_parser_name("mod")
NEG = Literal("-").set_parser_name("neg")
ADD = Literal("+").set_parser_name("add")
SUB = Literal("-").set_parser_name("sub")
BINARY_NOT = Literal("~").set_parser_name("binary_not")
BINARY_AND = Literal("&").set_parser_name("binary_and")
BINARY_OR = Literal("|").set_parser_name("binary_or")
GTE = Literal(">=").set_parser_name("gte")
LTE = Literal("<=").set_parser_name("lte")
LT = Literal("<").set_parser_name("lt")
GT = Literal(">").set_parser_name("gt")
EEQ = (
    Literal("==") | Literal("=")
).set_parser_name("eq")  # conservative equality  https://github.com/klahnakoski/jx-sqlite/blob/dev/docs/Logical%20Equality.md#definitions
DEQ = (
    Literal("<=>").set_parser_name("eq!")
)  # https://sparkbyexamples.com/apache-hive/hive-relational-arithmetic-logical-operators/
NEQ = (Literal("!=") | Literal("<>")).set_parser_name("neq")
LAMBDA = Literal("->").set_parser_name("lambda")

AND = keyword("and")
BETWEEN = keyword("between")
CASE = keyword("case").suppress()
COLLATE = keyword("collate")
END = keyword("end")
ELSE = keyword("else").suppress()
IN = keyword("in")
IS = keyword("is")
NOT = keyword("not")
OR = keyword("or")
LATERAL = keyword("lateral")
VIEW = keyword("view")

# COMPOUND KEYWORDS


joins = (
    (
        Optional(CROSS | OUTER | INNER | ((FULL | LEFT | RIGHT) + Optional(INNER | OUTER)))
        + JOIN
        + Optional(LATERAL)
    )
    | LATERAL + VIEW + Optional(OUTER)
) / (lambda tokens: " ".join(tokens).lower())


CREATE_TABLE = Group(CREATE + TABLE).set_parser_name("create_table")
UNION_ALL = (UNION + ALL).set_parser_name("union_all")
WITHIN_GROUP = Group(WITHIN + GROUP).set_parser_name("within_group")
SELECT_DISTINCT = Group(SELECT + DISTINCT).set_parser_name("select distinct")
PARTITION_BY = Group(PARTITION + BY).set_parser_name("partition by")
GROUP_BY = Group(GROUP + BY).set_parser_name("group by")
ORDER_BY = Group(ORDER + BY).set_parser_name("order by")

# COMPOUND OPERATORS
AT_TIME_ZONE = Group(keyword("at") + keyword("time") + keyword("zone"))
NOT_BETWEEN = Group(NOT + BETWEEN).set_parser_name("not_between")
NOT_LIKE = Group(NOT + LIKE).set_parser_name("not_like")
NOT_RLIKE = Group(NOT + RLIKE).set_parser_name("not_rlike")
NOT_IN = Group(NOT + IN).set_parser_name("nin")
IS_NOT = Group(IS + NOT).set_parser_name("is_not")

_SIMILAR = keyword("similar")
_TO = keyword("to")
SIMILAR_TO = Group(_SIMILAR + _TO).set_parser_name("similar_to")
NOT_SIMILAR_TO = Group(NOT + _SIMILAR + _TO).set_parser_name("not_similar_to")

RESERVED = MatchFirst([
    # ONY INCLUDE SINGLE WORDS
    ALL,
    AND,
    AS,
    ASC,
    BETWEEN,
    BY,
    CASE,
    COLLATE,
    CONSTRAINT,
    CREATE,
    CROSS,
    DESC,
    DISTINCT,
    EXCEPT,
    ELSE,
    END,
    FALSE,
    FOREIGN,
    FROM,
    FULL,
    GROUP_BY,
    GROUP,
    HAVING,
    IN,
    INDEX,
    INNER,
    INTERSECT,
    INTERVAL,
    IS_NOT,
    IS,
    JOIN,
    KEY,
    LATERAL,
    LEFT,
    LIKE,
    LIMIT,
    MINUS,
    NOCASE,
    NOT,
    NULL,
    OFFSET,
    ON,
    OR,
    ORDER,
    OUTER,
    OVER,
    PARTITION,
    PRIMARY,
    REFERENCES,
    RIGHT,
    RLIKE,
    SELECT,
    THEN,
    TRUE,
    UNION,
    UNIQUE,
    USING,
    WHEN,
    WHERE,
    WITH,
    WITHIN,
])

LB = Literal("(").suppress()
RB = Literal(")").suppress()
EQ = Char("=").suppress()

join_keywords = {
    "join",
    "full join",
    "cross join",
    "inner join",
    "left join",
    "right join",
    "full outer join",
    "right outer join",
    "left outer join",
}

precedence = {
    # https://www.sqlite.org/lang_expr.html
    "literal": -1,
    "cast": 0,
    "collate": 0,
    "concat": 1,
    "mul": 2,
    "div": 1.5,
    "mod": 2,
    "neg": 3,
    "add": 3,
    "sub": 2.5,
    "binary_not": 4,
    "binary_and": 4,
    "binary_or": 4,
    "gte": 5,
    "lte": 5,
    "lt": 5,
    "gt": 6,
    "eq": 7,
    "neq": 7,
    "missing": 7,
    "exists": 7,
    "at_time_zone": 8,
    "between": 8,
    "not_between": 8,
    "in": 8,
    "nin": 8,
    "is": 8,
    "like": 8,
    "not_like": 8,
    "rlike": 8,
    "not_rlike": 8,
    "similar_to": 8,
    "not_similar_to": 8,
    "and": 10,
    "or": 11,
    "lambda": 12,
    "select": 30,
    "from": 30,
    "window": 35,
    "union": 40,
    "union_all": 40,
    "except": 40,
    "minus": 40,
    "intersect": 40,
    "order": 50,
}


KNOWN_OPS = [
    COLLATE,
    CONCAT,
    MUL | DIV | MOD,
    NEG,
    ADD | SUB,
    BINARY_NOT,
    BINARY_AND,
    BINARY_OR,
    GTE | LTE | LT | GT,
    EEQ | NEQ | DEQ,
    AT_TIME_ZONE,
    (BETWEEN, AND),
    (NOT_BETWEEN, AND),
    IN,
    NOT_IN,
    IS_NOT,
    IS,
    LIKE,
    NOT_LIKE,
    RLIKE,
    NOT_RLIKE,
    SIMILAR_TO,
    NOT_SIMILAR_TO,
    NOT,
    AND,
    OR,
    LAMBDA,
]

times = ["now", "today", "tomorrow", "eod"]

durations = {
    "microseconds": "microsecond",
    "microsecond": "microsecond",
    "microsecs": "microsecond",
    "microsec": "microsecond",
    "useconds": "microsecond",
    "usecond": "microsecond",
    "usecs": "microsecond",
    "usec": "microsecond",
    "us": "microsecond",
    "milliseconds": "millisecond",
    "millisecond": "millisecond",
    "millisecon": "millisecond",
    "mseconds": "millisecond",
    "msecond": "millisecond",
    "millisecs": "millisecond",
    "millisec": "millisecond",
    "msecs": "millisecond",
    "msec": "millisecond",
    "ms": "millisecond",
    "seconds": "second",
    "second": "second",
    "secs": "second",
    "sec": "second",
    "s": "second",
    "minutes": "minute",
    "minute": "minute",
    "mins": "minute",
    "min": "minute",
    "m": "minute",
    "hours": "hour",
    "hour": "hour",
    "hrs": "hour",
    "hr": "hour",
    "h": "hour",
    "days": "day",
    "day": "day",
    "d": "day",
    "dayofweek": "dow",
    "dow": "dow",
    "weekday": "dow",
    "weeks": "week",
    "week": "week",
    "w": "week",
    "months": "month",
    "mons": "month",
    "mon": "month",
    "quarters": "quarter",
    "quarter": "quarter",
    "years": "year",
    "year": "year",
    "decades": "decade",
    "decade": "decade",
    "decs": "decade",
    "dec": "decade",
    "centuries": "century",
    "century": "century",
    "cents": "century",
    "cent": "century",
    "c": "century",
    "millennia": "millennium",
    "millennium": "millennium",
    "mils": "millennium",
    "mil": "millennium",
    "epoch": "epoch",
}

_size = Optional(LB + int_num("params") + RB)
_sizes = Optional(LB + delimited_list(int_num("params")) + RB)

# KNOWN TYPES
known_types = Forward()

BIGINT = Group(keyword("bigint")("op")) / to_json_call
BOOL = Group(keyword("bool")("op")) / to_json_call
BOOLEAN = Group(keyword("boolean")("op")) / to_json_call
DOUBLE = Group(keyword("double")("op")) / to_json_call
FLOAT64 = Group(keyword("float64")("op")) / to_json_call
FLOAT = Group(keyword("float")("op")) / to_json_call
GEOMETRY = Group(keyword("geometry")("op")) / to_json_call
INTEGER = Group(keyword("integer")("op")) / to_json_call
INT = Group(keyword("int")("op")) / to_json_call
INT32 = Group(keyword("int32")("op")) / to_json_call
INT64 = Group(keyword("int64")("op")) / to_json_call
REAL = Group(keyword("real")("op")) / to_json_call
TEXT = Group(keyword("text")("op")) / to_json_call
SMALLINT = Group(keyword("smallint")("op")) / to_json_call
STRING = Group(keyword("string")("op")) / to_json_call
STRUCT = Group(keyword("struct")("op")) / to_json_call

BLOB = (keyword("blob")("op") + _size) / to_json_call
BYTES = (keyword("bytes")("op") + _size) / to_json_call
CHAR = (keyword("char")("op") + _size) / to_json_call
VARCHAR = (keyword("varchar")("op") + _size) / to_json_call
VARBINARY = (keyword("varbinary")("op") + _size) / to_json_call
TINYINT = (keyword("tinyint")("op") + _size) / to_json_call

DECIMAL = (keyword("decimal")("op") + _sizes) / to_json_call
DOUBLE_PRECISION = (
    Group((keyword("double precision") / (lambda: "double_precision"))("op"))
    / to_json_call
)
NUMERIC = (keyword("numeric")("op") + _sizes) / to_json_call

MAP_TYPE = (
    keyword("map")("op") + LB + delimited_list(known_types("params")) + RB
) / to_json_call
ARRAY_TYPE = (keyword("array")("op") + LB + known_types("params") + RB) / to_json_call

DATE = keyword("date")
DATETIME = keyword("datetime")
TIME = keyword("time")
TIMESTAMP = keyword("timestamp")
TIMESTAMPTZ = keyword("timestamptz")
TIMETZ = keyword("timetz")

time_functions = DATE | DATETIME | TIME | TIMESTAMP | TIMESTAMPTZ | TIMETZ

# KNOWNN TIME TYPES
_format = Optional((ansi_string | ansi_ident)("params"))

DATE_TYPE = (DATE("op") + _format) / to_json_call
DATETIME_TYPE = (DATETIME("op") + _format) / to_json_call
TIME_TYPE = (TIME("op") + _format) / to_json_call
TIMESTAMP_TYPE = (TIMESTAMP("op") + _format) / to_json_call
TIMESTAMPTZ_TYPE = (TIMESTAMPTZ("op") + _format) / to_json_call
TIMETZ_TYPE = (TIMETZ("op") + _format) / to_json_call

known_types << MatchFirst([
    ARRAY_TYPE,
    BIGINT,
    BOOL,
    BOOLEAN,
    BLOB,
    BYTES,
    CHAR,
    DATE_TYPE,
    DATETIME_TYPE,
    DECIMAL,
    DOUBLE_PRECISION,
    DOUBLE,
    FLOAT64,
    FLOAT,
    GEOMETRY,
    MAP_TYPE,
    INTEGER,
    INT,
    INT32,
    INT64,
    NUMERIC,
    REAL,
    TEXT,
    SMALLINT,
    STRING,
    STRUCT,
    TIME_TYPE,
    TIMESTAMP_TYPE,
    TIMESTAMPTZ_TYPE,
    TIMETZ_TYPE,
    VARCHAR,
    VARBINARY,
    TINYINT,
])

CASTING = (Literal("::").suppress() + known_types("params")).set_parser_name("cast")
KNOWN_OPS = [CASTING] + KNOWN_OPS
offset = Forward()

unary_ops = {
    NEG: RIGHT_ASSOC,
    NOT: RIGHT_ASSOC,
    BINARY_NOT: RIGHT_ASSOC,
    CASTING: LEFT_ASSOC,
}

from mo_sql_parsing import utils

utils.unary_ops = unary_ops
del utils

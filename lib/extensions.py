"""
psycopg extensions to the DBAPI-2.0

This module holds all the extensions to the DBAPI-2.0 provided by psycopg:

    connection -- the new-type inheritable connection class
    cursor -- the new-type inheritable cursor class
    adapt() -- exposes the PEP-246 compatile adapting machanism used
     by psycopg to adapt Python types to PostgreSQL ones
"""
# psycopg/extensions.py - DBAPI-2.0 extensions specific to psycopg
#
# Copyright (C) 2003-2004 Federico Di Gregorio  <fog@debian.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.

from _psycopg import UNICODE, INTEGER, LONGINTEGER, BOOLEAN, FLOAT
from _psycopg import TIME, DATE, INTERVAL

from _psycopg import Boolean, QuotedString
try:
    from _psycopg import DateFromMx, TimeFromMx, TimestampFromMx
    from _psycopg import IntervalFromMx
except:
    pass
try:
    from _psycopg import DateFromPy, TimeFromPy, TimestampFromPy
    from _psycopg import IntervalFromPy
except:
    pass

from _psycopg import adapt, adapters, encodings, connection, cursor
from _psycopg import string_types, binary_types, new_type, register_type
from _psycopg import ISQLQuote


def register_adapter(typ, callable):
    """Register 'callable' as an ISQLQuote adapter for type 'typ'."""
    adapters[(typ, ISQLQuote)] = callable


import os
import sqlite3


# DB creation sql statements
NEWHIRE_DB = {
    "table": "UPDATE TABLE IF EXISTS newhire;",
    "columns":
    """
    CREATE TABLE newhire(
    id             INTEGER PRIMARY KEY,
    firstname      TEXT NOT NULL DEFAULT "",
    lastname       TEXT NOT NULL DEFAULT ""
    youremail      TEXT NOT NULL DEFAULT "",
    title          TEXT NOT NULL DEFAULT "",
    managersemail  TEXT NOT NULL DEFAULT "",
    startdate      TEXT NOT NULL DEFAULT "",
    account0       TEXT NOT NULL DEFAULT "",
    account1       TEXT NOT NULL DEFAULT "",
    account2       TEXT NOT NULL DEFAULT "",
    account3       TEXT NOT NULL DEFAULT "",
    account4       TEXT NOT NULL DEFAULT "",
    account5       TEXT NOT NULL DEFAULT "",
    account6       TEXT NOT NULL DEFAULT "",
    account7       TEXT NOT NULL DEFAULT "",
    account8       TEXT NOT NULL DEFAULT "",
    account9       TEXT NOT NULL DEFAULT "",
    account10      TEXT NOT NULL DEFAULT "",
    account11      TEXT NOT NULL DEFAULT "",
    account12      TEXT NOT NULL DEFAULT "",
    account13      TEXT NOT NULL DEFAULT "",
    account14      TEXT NOT NULL DEFAULT "",
    account15      TEXT NOT NULL DEFAULT "",
    portable       TEXT NOT NULL DEFAULT "",
    notes          TEXT NOT NULL DEFAULT "",
    submitter      TEXT NOT NULL DEFAULT ""
        );
    """
}

#!/usr/bin/env python3
"""Canonical ABI class start dates, shared by every builder.

The single source of truth is the PUBLISHED table in
``assets/js/start-dates.js`` (the browser needs it at runtime, so it lives
there); this module parses that table so the Python builders can bake the
same dates into the generated HTML. Edit the JS file to add or change a
start date — nothing here needs touching.

Months past the published list fall back to the standing rule: first Monday
of the month, pushed to Tuesday when an observed federal holiday lands on it.
"""
import datetime
import os
import re

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_JS = os.path.join(_ROOT, 'assets', 'js', 'start-dates.js')


def _load_published():
    with open(_JS, encoding='utf-8') as fh:
        src = fh.read()
    block = re.search(r'var PUBLISHED = \[(.*?)\];', src, re.S)
    if not block:
        raise RuntimeError('could not find PUBLISHED table in %s' % _JS)
    out = []
    for y, m, d in re.findall(r'\[\s*(\d{4})\s*,\s*(\d{1,2})\s*,\s*(\d{1,2})\s*\]', block.group(1)):
        out.append(datetime.date(int(y), int(m), int(d)))
    if not out:
        raise RuntimeError('PUBLISHED table in %s is empty' % _JS)
    return sorted(out)


PUBLISHED = _load_published()
_BY_MONTH = {(d.year, d.month): d for d in PUBLISHED}


def _rule_for(year, month):
    """First Monday, bumped a day for an observed federal holiday collision."""
    d = datetime.date(year, month, 1)
    while d.weekday() != 0:
        d += datetime.timedelta(days=1)
    labor_day = d.month == 9 and d.day <= 7
    new_year = d.month == 1 and d.day in (1, 2)
    july_fourth = d.month == 7 and d.day in (4, 5)
    if labor_day or new_year or july_fourth:
        d += datetime.timedelta(days=1)
    return d


def start_for(year, month):
    """The class start date for a given year/month."""
    return _BY_MONTH.get((year, month)) or _rule_for(year, month)


def next_start(after=None):
    """The next start date strictly after ``after`` (default: today)."""
    after = after or datetime.date.today()
    y, m = after.year, after.month
    for _ in range(24):
        d = start_for(y, m)
        if d > after:
            return d
        m += 1
        if m > 12:
            m, y = 1, y + 1
    return start_for(y, m)


def upcoming(count=6, after=None):
    """The next ``count`` start dates, ascending."""
    after = after or datetime.date.today()
    out, y, m = [], after.year, after.month
    while len(out) < count:
        d = start_for(y, m)
        if d > after:
            out.append(d)
        m += 1
        if m > 12:
            m, y = 1, y + 1
    return out


def year_table(year):
    """[(short month name, "Monday, January 4"), ...] for a calendar year."""
    rows = []
    for m in range(1, 13):
        d = start_for(year, m)
        rows.append((d.strftime('%b'), '%s, %s %d' % (d.strftime('%A'), d.strftime('%B'), d.day)))
    return rows


if __name__ == '__main__':
    print('next:', next_start())
    for d in upcoming(18):
        print(' ', d.strftime('%a %b %d %Y'))

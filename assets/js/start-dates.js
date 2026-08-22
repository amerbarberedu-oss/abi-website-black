/* American Barber Institute — canonical class start dates.
   ------------------------------------------------------------------
   Single source of truth for every "next class starts" date, countdown
   target and start-date list on the site. Published by ABI through
   Dec 2027; months past the published list fall back to the standing
   rule (first Monday of the month, pushed to Tuesday when a federal
   holiday lands on it — that is exactly why Sep 8 2026, Jul 6 2027 and
   Sep 7 2027 are Tuesdays).

   Keep the mirrors in sync when this list is extended:
     src/build.py            (baked-in next start + countdown)
     src/build_landing_pages.py (funnel next start + calendar table)
*/
(function (root) {
  'use strict';

  /* Published start dates, ascending. [year, month (1-12), day] */
  var PUBLISHED = [
    [2026, 9, 8], [2026, 10, 5], [2026, 11, 2], [2026, 12, 7],
    [2027, 1, 4], [2027, 2, 1], [2027, 3, 1], [2027, 4, 5],
    [2027, 5, 3], [2027, 6, 7], [2027, 7, 6], [2027, 8, 2],
    [2027, 9, 7], [2027, 10, 4], [2027, 11, 1], [2027, 12, 6]
  ];

  function at(y, m, d) { return new Date(y, m - 1, d, 0, 0, 0, 0); }

  /* Fallback for months beyond the published list: first Monday, bumped a
     day when it collides with an observed federal holiday (New Year's Day,
     Independence Day, Labor Day). */
  function ruleFor(y, m) {
    var d = at(y, m, 1);
    while (d.getDay() !== 1) d.setDate(d.getDate() + 1);
    var mo = d.getMonth() + 1, day = d.getDate();
    var isLaborDay = (mo === 9 && day <= 7);
    var isNewYear = (mo === 1 && (day === 1 || day === 2));   // Jan 1, or Mon observance of a Sun Jan 1
    var isJulyFourth = (mo === 7 && (day === 4 || day === 5)); // Jul 4, or Mon observance of a Sun Jul 4
    if (isLaborDay || isNewYear || isJulyFourth) d.setDate(d.getDate() + 1);
    return d;
  }

  function startFor(y, m) {
    for (var i = 0; i < PUBLISHED.length; i++) {
      if (PUBLISHED[i][0] === y && PUBLISHED[i][1] === m) {
        return at(PUBLISHED[i][0], PUBLISHED[i][1], PUBLISHED[i][2]);
      }
    }
    return ruleFor(y, m);
  }

  /* Next start strictly after `from` (defaults to now). */
  function next(from) {
    var now = from || new Date();
    var y = now.getFullYear(), m = now.getMonth() + 1;
    for (var i = 0; i < 24; i++) {
      var d = startFor(y, m);
      if (d > now) return d;
      m++; if (m > 12) { m = 1; y++; }
    }
    return startFor(y, m);
  }

  /* The next `count` start dates, ascending. */
  function upcoming(count, from) {
    var now = from || new Date();
    var out = [], y = now.getFullYear(), m = now.getMonth() + 1;
    while (out.length < (count || 6)) {
      var d = startFor(y, m);
      if (d > now) out.push(d);
      m++; if (m > 12) { m = 1; y++; }
    }
    return out;
  }

  root.ABIStartDates = { published: PUBLISHED, startFor: startFor, next: next, upcoming: upcoming };
})(window);

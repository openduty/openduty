# Contributing to openduty

**Please note:** 

**First:** if you're unsure or afraid of _anything_, just ask or submit the
issue or pull request anyways. You won't be yelled at for giving it your best
effort. The worst that can happen is that you'll be politely asked to change
something. We appreciate any sort of contributions, and don't want a wall of
rules to get in the way of that. 

This document will cover what we're looking for in terms of reporting issues.
By addressing all the points we're looking for, it raises the chances we can
quickly merge or address your contributions.

## Issues

### Reporting an Issue

* Make sure you test against the latest released version. It is possible
  we already fixed the bug you're experiencing. Even better is if you can test
  against `master`, as bugs are fixed regularly but new versions are only
  released every few months.

* Provide steps to reproduce the issue, and if possible include the expected 
  results as well as the actual results. Please provide text, not screen shots!

* If you are seeing an internal `openduty` error (a status code of 5xx), please be
  sure to post relevant parts of (or the entire) `openduty` log, as often these
  errors are logged on the server but not reported to the user

* Respond as promptly as possible to any questions made by the `openduty`
  team to your issue. Stale issues will be closed periodically.

### Issue Lifecycle

1. The issue is reported.

2. The issue is verified and categorized by an `openduty` collaborator.
   Categorization is done via tags. For example, bugs are marked as "bugs".

3. Unless it is critical, the issue may be left for a period of time (sometimes
   many weeks), giving outside contributors -- maybe you!? -- a chance to
   address the issue.

4. The issue is addressed in a pull request or commit. The issue will be
   referenced in the commit message so that the code that fixes it is clearly
   linked.

5. The issue is closed. Sometimes, valid issues will be closed to keep
   the issue tracker clean. The issue is still indexed and available for
   future viewers, or can be re-opened if necessary.

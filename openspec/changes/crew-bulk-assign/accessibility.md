## Keyboard path

Tab to the first row, Space to toggle, Shift+Space to extend, `A` to select all visible,
Escape to clear, Enter to open the crew chooser. The whole flow is completable without
a pointer.

## Focus order

Row → row → action bar (once a selection exists) → crew chooser → confirm. On error,
focus moves to the first offending row, not to the error banner, so the next action is
one keystroke away.

## Focus traps

The confirmation dialog traps focus and returns it to the action bar on cancel. The
10-second undo does not steal focus.

## Screen reader announcements

Selection changes announce the running count ("12 bookings selected"), not each row.
Applying announces once at start and once at completion. The error announces the count
and the reason, then the offending booking.

## Contrast

Selected-row background against row text: 7.1:1. The action bar's disabled Cancel during
applying: 4.6:1, which meets AA for non-text UI at that size.

## Target sizes

Row checkboxes are 24x24 CSS px with a 44x44 hit area. The action bar buttons are 44px
tall.

## Knowingly not met

WCAG 2.2 **2.5.7 Dragging Movements** — there is no drag affordance here at all, so the
criterion does not apply rather than being unmet. No criterion is knowingly failed.

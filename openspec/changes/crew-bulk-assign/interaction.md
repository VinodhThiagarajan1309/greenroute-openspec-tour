## States

| state | shown | person can | next |
|---|---|---|---|
| default | the day's bookings, none selected | select any row | selecting |
| selecting | n selected, action bar visible with the count | add/remove, clear, choose a crew | confirming |
| confirming | "Move 12 bookings to Crew B?" with the list | confirm or cancel | applying |
| applying | rows dimmed, action bar shows progress | cancel is disabled | success or error |
| success | rows moved, "12 bookings moved to Crew B. Undo." | undo for 10s | default |
| error | nothing moved, reason stated per offending booking | fix selection or cancel | selecting |
| empty | "No bookings scheduled for this day" | change the date | default |

## Transitions

Selection survives a crew filter change; it does **not** survive a date change, because
a booking on another date is not the one the dispatcher looked at. Partial application
is not a state: a bulk move either applies wholly or not at all.

## Keyboard path

Tab reaches the first row. Space toggles selection. Shift+Space extends. `A` selects
all visible. Escape clears selection. Enter opens the crew chooser. The action bar is
reachable by Tab from any selected row without passing through the remaining rows.

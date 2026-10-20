## 1. States

- [x] 1.1 Default, selecting and empty states; verify each renders from fixture data
- [x] 1.2 Confirming, applying, success and error states; verify the state machine test covers every transition in interaction.md

## 2. Behaviour

- [x] 2.1 Selection survives a crew filter change and clears on a date change; verify the two scenarios in the delta
- [x] 2.2 Whole-batch rejection on a licence-gate failure; verify the pesticide-in-a-batch scenario

## 3. Accessibility

- [x] 3.1 Keyboard path completes the flow with no pointer; verify by keyboard-only walkthrough
- [x] 3.2 Focus moves to the first offending row on error; verify in the error-state test
- [x] 3.3 Count-based announcements, not per-row; verify with a screen reader on the selecting state
- [x] 3.4 Contrast and target sizes as recorded; verify with the contrast checker and a 44px overlay

## 4. Verification

- [x] 4.1 Every state in interaction.md has a test; verify the state machine test enumerates them

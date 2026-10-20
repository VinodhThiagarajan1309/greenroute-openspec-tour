## Observed

41m12s (Spark) vs 38s (DuckDB). Zero disagreeing rows across 2.8M. Memory peaked
at 4.1GB.

## Surprises

Parquet predicate pushdown did most of the work. The engine mattered less than not
re-reading history.

## Interpretation

The win is bounded by memory, not by engine. At 10x rows it does not hold.

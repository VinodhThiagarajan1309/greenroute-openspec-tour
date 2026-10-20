## What will be run

The existing parity query against a DuckDB read of the same Parquet files.

## On what data / environment

One month of `gold_payment_ledger` (2.8M rows), laptop, 16GB.

## The number being read

Wall-clock seconds, and the count of disagreeing rows versus Spark.

## Deliberately not building

No orchestration, no incremental mode, no deployment. The code is thrown away.

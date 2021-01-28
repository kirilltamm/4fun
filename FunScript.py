import sentry_sdk
sentry_sdk.init(
    "https://94fec882847a485c9fd8a71b1d57598c@o503592.ingest.sentry.io/5612629",
    traces_sample_rate=1.0
)

division_by_zero = 1 / 0
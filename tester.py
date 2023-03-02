import sentry_sdk
sentry_sdk.init(
    dsn="https://a9ee78acce5c4aa1a36cb471e9ba5d23@o4504765715316736.ingest.sentry.io/4504765725671424",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)

# division_by_zero = 1 / 0

a = []
a[0]

print("No Errors!")

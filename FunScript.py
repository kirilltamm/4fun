import sentry_sdk
import logging
from sentry_sdk.integrations.logging import LoggingIntegration
sentry_sdk.init(
    "https://94fec882847a485c9fd8a71b1d57598c@o503592.ingest.sentry.io/5612629",
    traces_sample_rate=1.0
)

logging.basicConfig(level='DEBUG')

logger = logging.getLogger()

def main(name):
	print(logger.handlers)
	logger.critical(f'Enter in the main() function: name = {name}')
	logger.error('this is an error messege')
	logger.warning('this is an warning messege')



if __name__ == '__main__':
	main('kirill')

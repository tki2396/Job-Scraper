from typing import Any
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext

tracer = Tracer()
logger = Logger(service="scaper/crawlers")

from ingestion.config import get_settings

settings = get_settings()

@tracer.capture_lambda_handler
def handler(event, context: LambdaContext | None = None) -> dict[str, Any]:
    logger.info(f"Begin crawling {event}")
    return {
        'status': 200,
        'data': 'Hello world'
    }

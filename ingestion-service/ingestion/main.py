from typing import Any
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger(service="scaper/crawlers")

from ingestion.config import get_settings
from ingestion.crawlers.linkedin import LinkedinCrawler

settings = get_settings()

def handler(event, context: LambdaContext | None = None) -> dict[str, Any]:
    return {
        'status': 200,
        'data': 'Hello world'
    }
    # crawler = LinkedinCrawler()
    # link = "https://www.linkedin.com/in/tobi-ijose-679a75132/"
    # user = {
    #     "username": settings.LINKEDIN_USERNAME,
    # }
    # crawler.extract(link, user=user)


# if __name__ == "__main__":
#     main()

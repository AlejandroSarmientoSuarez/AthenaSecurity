from contextlib import asynccontextmanager

from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle."""

    logger.info("Starting Athena API...")

    # TODO:
    # Initialize database connections.
    # Initialize AI providers.
    # Initialize caches.

    yield

    logger.info("Stopping Athena API...")

    # TODO:
    # Close database connections.
    # Release resources.
from typing import Optional
from dataclasses import dataclass

from ..responses import KeyValuePair, KeyValuePairInput


@dataclass(kw_only=True)
class AnalyticsProvider:
    isEnabled: bool                                 # Is the provider active
    key: str                                        # Unique identifier for this provider
    props: Optional[list[str]] = None               # List of configuration properties, formatted as strified JSON objects
    title: str                                      # Name of the provider
    description: Optional[str] = None               # Short description of the provider
    isAvailable: Optional[bool] = None              # Is the provider available for use
    logo: Optional[str] = None                      # Path to the provider logo
    website: Optional[str] = None                   # Website of the provider
    config: Optional[list[KeyValuePair]] = None     # Configuration values for this provider


@dataclass(kw_only=True)
class AnalyticsProviderInput:
    isEnabled: bool                                         # Is the provider active
    key: str                                                # Unique identifier of the provider
    config: Optional[list[KeyValuePairInput]] = None        # Configuration values for this provider

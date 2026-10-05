"""Team Profile PDF extraction tools.

This package provides tools for extracting Team Profile employee profile
data from PDF files and converting them to JSON format with interpretations.
"""

from team_profile.constants import ARCHETYPES
from team_profile.extract import generate_json, process_pdf
from team_profile.models import ExtractionResult
from team_profile.opencv_extractor import extract_with_opencv

__version__ = "0.1.0"

__all__ = [
    "ARCHETYPES",
    "ExtractionResult",
    "extract_with_opencv",
    "generate_json",
    "process_pdf",
]

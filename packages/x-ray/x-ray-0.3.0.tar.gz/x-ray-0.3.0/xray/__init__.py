"""
Find bad redactions.
"""

from pathlib import Path
from typing import Union

from fitz import Document

from .custom_types import PdfRedactionsDict
from .pdf_utils import get_bad_redactions


def inspect(file: Union[str, bytes, Path]) -> PdfRedactionsDict:
    """
    Inspect a file for bad redactions and return a Dict with their info

    :file: The PDF to process, as bytes if you have the file in memory (useful
    if it's coming from the network),, as a unicode string if you know the
    path to the file on your local disk, or as a pathlib.Path object.
    :return: A dict with the bad redaction information. If no bad redactions
    are found, returns an empty dict.
    """
    if type(file) == bytes:
        pdf = Document(stream=file, filetype="pdf")
    else:
        pdf = Document(file)

    bad_redactions = {}
    for page_number, page in enumerate(pdf, start=1):
        redactions = get_bad_redactions(page)
        if redactions:
            bad_redactions[page_number] = redactions
    pdf.close()

    return bad_redactions

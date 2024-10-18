"""
Violent Reductioniser text strings

Author: Arsalan 'Aeri' Kazmi <https://aeriavelocity.github.io>
Licence: GPL-3.0-or-later

This file is part of Violent Reductioniser.
"""

import locale

locale.setlocale(locale.LC_ALL, "")

# British English (en_GB) by default
STRINGS = {
    "title": "Violent Reductioniser",
    "cwd_label": "Current working directory: ",
    "input_label": "Original video file:",
    "output_label": "Destination file:",
    "reductionise_button": "Reductionise",
    "browse_button": "Browse...",
    "browse_input_title": "Select original video file",
    "browse_output_title": "Select destination file",
    "error_title": "Error",
    "missing_fields": "No input or output file specified.",
    "file_not_found": "Input file {} not found",
    "input_is_output": "Input and output files cannot be the same.",
    "warning_title": "Warning!!",
    "warning_message": "Proceeding with this operation will result in \
utter devastation of your original video file. \
This WILL result in loss of data. (Your original file is still safe, though.)",
    "ffmpeg_error": "FFmpeg error",
    "success_title": "Success!",
    "success_message": "The video has been successfully reductionised."
}

if locale.getlocale()[0] == "en_US":
    STRINGS.title = "Violent Reductionizer"
    STRINGS.reductionise_button = "Reductionize"
    STRINGS.success_message = "The video has been successfully reductionized."

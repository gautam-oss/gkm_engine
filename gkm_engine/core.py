"""Core logic for gkm_engine."""

from __future__ import annotations

import platform
import sys
from datetime import datetime, timezone


def run() -> None:
    """Entry point for both the Python API and the `gkm` CLI command.

    Prints a brief status report and exits cleanly.
    """
    print(_build_report())


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _build_report() -> str:
    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    return (
        "\n"
        "╔══════════════════════════════════════╗\n"
        "║          gkm_engine  v0.1.0          ║\n"
        "╚══════════════════════════════════════╝\n"
        f"  Python   : {sys.version.split()[0]}\n"
        f"  Platform : {platform.system()} {platform.release()}\n"
        f"  Time     : {now}\n"
        "\n"
        "  Engine started successfully. ✓\n"
    )
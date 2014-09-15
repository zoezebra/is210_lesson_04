#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""I am a docstring."""

import data

TOTAL_WORDS = float(len(data.SHAKESPEARE.split()))
LINES = 0
MINIMUM_WORDS = None
MAXIMUM_WORDS = 0
NUM_CRISPIAN = 0
for line in data.SHAKESPEARE.split('\n'):
    LINES += 1

    WORDS = len(line.split())

    if WORDS > MAXIMUM_WORDS:
        MAXIMUM_WORDS = WORDS

    if WORDS < MINIMUM_WORDS or MINIMUM_WORDS is None:
        MINIMUM_WORDS = WORDS

    if 'Crispian' in line:
        NUM_CRISPIAN += 1

AVERAGE_WORDS = TOTAL_WORDS / LINES

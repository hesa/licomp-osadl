#!/bin/env python3

# SPDX-FileCopyrightText: 2024 Henrik Sandklef
# SPDX-License-Identifier: GPL-3.0-only

import os
import json
import urllib3

MATRIX_URL = 'https://www.osadl.org/fileadmin/checklists/matrixseqexpl.json'
VAR_DIR = os.path.join(os.path.dirname(__file__), '..')
VAR_DIR = os.path.join(VAR_DIR, 'licomp_osadl')
VAR_DIR = os.path.join(VAR_DIR, 'var')
MATRIX_FILE=os.path.join(VAR_DIR, 'matrixseqexpl.json')


http = urllib3.PoolManager()
resp = http.request('GET', MATRIX_URL)
matrix_data = json.loads(resp.data.decode('utf-8'))
with open(MATRIX_FILE, 'w') as jsonfile:
    json.dump(matrix_data, jsonfile, indent=4, sort_keys=True)


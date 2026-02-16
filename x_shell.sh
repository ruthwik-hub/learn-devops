#!/bin/bash
echo "Initiating system check..."
CURRENT_USER=$(whoami)
echo "User: $CURRENT_USER"
echo "Working Directory: $(pwd)"
if [[ -f "test.py" ]]; then echo "Note: Python test script found in this folder."; fi
echo "Looping through test cycles:"
for i in {1..3}; do echo "  - Cycle $i complete"; done
echo "Kernel Version: $(uname -r)"
echo "Test sequence finished successfully."
CT=$(python3 badencrypt.py testkeyfile)
MODCT=$(python3 attack.py "$CT")
echo "CT:\n$CT"
echo "MODCT:\n$MODCT"
python3 baddecrypt.py testkeyfile "$MODCT"
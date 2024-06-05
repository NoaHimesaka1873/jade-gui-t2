#!/usr/bin/bash
echo | tee /tmp/jade-gui-output.txt &>/dev/null
echo "Starting installation with blend-inst..." | tee -a /tmp/jade-gui-output.txt
echo "Errors might appear every once in a while during installation, but that's perfectly normal." | tee -a /tmp/jade-gui-output.txt
echo | tee -a /tmp/jade-gui-output.txt
sudo blend-inst config ~/.config/jade.json | tee -a /tmp/jade-gui-output.txt

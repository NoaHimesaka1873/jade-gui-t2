#!/usr/bin/bash
echo | tee /tmp/jade-gui-output.txt &>/dev/null
echo "Starting installation with blend-inst..." | tee -a /tmp/jade-gui-output.txt
echo "Errors might appear every once in a while during installation, but that's perfectly normal." | tee -a /tmp/jade-gui-output.txt
sleep 3
echo | tee -a /tmp/jade-gui-output.txt
script -a -c "sudo blend-inst config ~/.config/jade.json" /tmp/jade-gui-output.txt

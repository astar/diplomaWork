#/bin/bash
a=0;for i in *.pdf; do mv $i tmp/$((++a)).pdf;done
mv tmp/* .
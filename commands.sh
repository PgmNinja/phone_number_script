#! /bin/bash

BIN=/bin
sudo cp ./commands/* $BIN
sudo chmod +x $BIN/encode_phone $BIN/decode_phone

mkdir $HOME/.nir_scripts
cp -r ./* $HOME/.nir_scripts

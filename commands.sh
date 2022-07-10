#! /bin/bash

BIN=/bin
sudo cp ./commands/* $BIN
sudo chmod +x $BIN/nir_script_encode_phone $BIN/nir_script_decode_phone

[ -d "$HOME/.nir_scripts" ] && rm -r $HOME/.nir_scripts
mkdir $HOME/.nir_scripts
cp -r ./* $HOME/.nir_scripts

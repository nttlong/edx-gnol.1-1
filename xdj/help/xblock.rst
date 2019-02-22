
cd {source}
sudo ./use_edx
source ./apps/edx/venvs/edxapp/bin/activate
cd /apps/edx/venvs/edxapp

git clone https://github.com/MarCnu/pdfXBlock.git

pip install -e ./pdfXBlock

git clone https://github.com/eduNEXT/flow-control-xblock.git

cd flow-control-xblock

pip install -r requirements.txt

cd..

git clone https://github.com/edx-solutions/xblock-ooyala.git

cd xblock-ooyala

pip install -r requirements.txt

git clone https://github.com/oppia/xblock.git

cd xblock

pip install -r requirements.txt

cd ..

git clone https://github.com/ExtensionEngine/xblock_charting.git

cd xblock_charting

pip install -e piechart

cd ..


git clone https://github.com/open-craft/problem-builder.git

cd problem-builder

pip install -r requirements.txt



cd {source}
sudo ./use_edx
source ./apps/edx/venvs/edxapp/bin/activate
cd /apps/edx/venvs/edxapp

git clone https://github.com/MarCnu/pdfXBlock.git

pip install -e ./pdfXBlock

sudo -H pip install git+https://github.com/MarCnu/pdfXBlock
sudo -H pip install git+https://github.com/OfficeDev/xblock-officemix.git

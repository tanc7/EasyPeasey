echo Changing to root directory
# PupyHome() {
#   cd /root/
# }
echo Cloning Pupy Git Repo
git clone https://github.com/n1nj4sec/pupy
cd pupy
echo Initializing and Updating submodules
git submodule init
git submodule update
echo Installing Python module requirements
pip install -r /root/pupy/pupy/requirements.txt
echo Done. If this is your first time, please restart ArmsCommander and attempt to run the Pupy-Generator

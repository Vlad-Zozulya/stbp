
# install fkae8 and radon packages
pip install pyarmor pyminifier

# run pyarmor
pyarmor obfuscate file.py

# run pyminifier
pyminifier --obfuscate-classes --obfuscate-functions --obfuscate-import-methods file.py > file_obfuscated.py

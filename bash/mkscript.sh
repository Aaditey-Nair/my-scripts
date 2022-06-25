#!/usr/bin/zsh

echo "#!/usr/bin/zsh

echo 'this is a script'" > $1.sh

chmod u+x $1.sh

nano $1.sh

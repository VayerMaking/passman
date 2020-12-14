#!/usr/bin/env bash

LOCATION=$1
if [[ -z $LOCATION ]]; then
    echo "Usage: $0 <venv_folder>"
    exit 0
fi

FILE=`find ${LOCATION} -type f -name "activate"`

if [[ -z $FILE ]]; then
    echo "We don't have venv in $LOCATION -> $FILE"
else
    echo "Loading VENV from $FILE"
    echo "Use Ctrl-D to deactivate"
    PROMPT='(venv) ${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
    bash -c ". ${FILE}; exec /usr/bin/env bash --rcfile <(echo 'PS1=\"${PROMPT}\"') -i"
fi

#!/usr/bin/env bash
DIRECTORY=virtualenvs/.dialog-builder
deactivate 2> /dev/null
if [ -d "${DIRECTORY}" ]; then
    source ${DIRECTORY}/bin/activate
else
    virtualenv -p `which python3` ${DIRECTORY}
    source ${DIRECTORY}/bin/activate
fi

export APP_NAME="DialogBuilder"
export APP_ENV="DEV-${USER}"

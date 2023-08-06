#!/bin/bash -e

if [ -z "$SPOTML_CONTAINER_NAME" ]; then
  echo -e "\nSPOTML_CONTAINER_NAME environmental variable is not set.\n"
  exit 1
fi

SPOTML_CONTAINER_WORKING_DIR=${SPOTML_CONTAINER_WORKING_DIR:-/}

{{{docker_exec_bash}}}

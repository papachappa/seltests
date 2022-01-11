#!/bin/bash

[[ "$BASH_SOURCE" == "$0" ]] && {
    echo "Please 'source' this script, don't execute it directly"
    echo "e.g.:"
    echo "$ source $0"
    return 1 2> /dev/null || exit 1
}

export OS_AUTH_URL="https://api.selvpc.ru/identity/v3"

export OS_IDENTITY_API_VERSION="3"
export OS_VOLUME_API_VERSION="3"

export CLIFF_FIT_WIDTH=1

export OS_PROJECT_DOMAIN_NAME='168063'
export OS_PROJECT_ID='a0369ddcf5d34c089430ddc239863a72'
export OS_TENANT_ID='a0369ddcf5d34c089430ddc239863a72'
export OS_REGION_NAME='ru-9'

export OS_USER_DOMAIN_NAME='168063'
export OS_USERNAME='QA_user'
export OS_PASSWORD='test123'

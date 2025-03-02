#!/sbin/openrc-run

name="myprod"
description="MyProd Docker Compose Service"

command="/usr/bin/docker-compose"
command_args="-f /docker/prod/docker-compose.yml up -d"
pidfile="/run/${RC_SVCNAME}.pid"

start_pre() {
    checkpath --directory --mode 0755 /docker/prod
    if /usr/bin/docker network inspect prod_myprod-net >/dev/null 2>&1; then
        ebegin "Removing existing Docker network"
        /usr/bin/docker network rm prod_myprod-net
        eend $?
    fi
}

start() {
    ebegin "Starting ${name}"
    /usr/bin/docker-compose -f /docker/prod/docker-compose.yml up -d
    eend $?
}

stop() {
    ebegin "Stopping ${name}"
    /usr/bin/docker-compose -f /docker/prod/docker-compose.yml down
    eend $?
}


import time
import shlex, subprocess
import random
import pytest

from  pathlib import Path


VM_LOCAL_DISK_NAME = 'test_srv_with_boot_local' + str(random.randint(1, 1000))
VM_NET_DISK_NAME = 'test_srv_with_boot_net_volume_add_volume' + str(random.randint(1, 1000))
BOOT_DISK_NAME = 'BOOT_DISK' + str(random.randint(1, 1000))
ADD_DISK_NAME = 'ADD_DISK_NAME' + str(random.randint(1, 1000))


@pytest.fixture(scope="class")
def exec_rc_file():
    CWD = Path(__file__).resolve().parent
    rc_script = Path(CWD, "rc.sh").chmod(0o0777)
    output = subprocess.Popen(["bash", "-c", "source {}".format(rc_script)])


@pytest.fixture
def create_vm_local_disk(request):
    args = f"""
        openstack server create \
        --availability-zone ru-9a \
        --flavor SL1.2-4096-32 \
        --nic net-id={request.param} \
        --image 'Ubuntu 20.04 LTS 64-bit' {VM_LOCAL_DISK_NAME}
    """
    cmd = shlex.split(args)
    output = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    yield
    delete_vm_local_disk()


def delete_vm_local_disk():
    args = f"openstack server delete {VM_LOCAL_DISK_NAME}"
    cmd = shlex.split(args)
    output = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


@pytest.fixture
def create_vm_net_disk(request):
    args = f"openstack volume create --image 'Ubuntu 20.04 LTS 64-bit' --size 5 --type basic.ru-9a {BOOT_DISK_NAME}"
    cmd = shlex.split(args)
    output = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    args = f"openstack volume create --size 20 --type basic.ru-9a {ADD_DISK_NAME}"
    cmd = shlex.split(args)
    output = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    args = f"""
        openstack server create \
        --availability-zone ru-9a \
        --flavor SL1.2-4096-32 \
        --nic net-id={request.param} \
        --block-device-mapping vdb={ADD_DISK_NAME} \
        --volume {BOOT_DISK_NAME} \
        {VM_NET_DISK_NAME}

    """
    cmd = shlex.split(args)
    output = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    yield
    delete_vm_net_disk()


def delete_vm_net_disk():
    args = f"openstack server delete {VM_NET_DISK_NAME}"
    cmd = shlex.split(args)
    output = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # wait for main vm deletion
    time.sleep(10)

    args = f"openstack volume delete {ADD_DISK_NAME}"
    cmd = shlex.split(args)
    output = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    args = f"openstack volume delete {BOOT_DISK_NAME}"
    cmd = shlex.split(args)
    output = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def list_servers():
    args = "openstack server list"
    cmd = shlex.split(args)
    output = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = output.communicate()
    return out


@pytest.fixture
def check_vm_status(request):
    timeout = 15
    while timeout:
        output = list_servers()
        if request.param in output.decode().lower():
            return output
        timeout -= 1


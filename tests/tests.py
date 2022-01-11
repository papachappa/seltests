import pytest


@pytest.mark.usefixtures('exec_rc_file')
class  TestSelectelVMs():
    @pytest.mark.parametrize('create_vm_local_disk', ["c1445f3f-090b-4104-98ab-2840cf121f0d"], indirect=True)
    @pytest.mark.parametrize('check_vm_status', ["active"], indirect=True)
    def test_create_vm_local_disk(self, create_vm_local_disk, check_vm_status):
        assert check_vm_status

    @pytest.mark.parametrize('create_vm_net_disk', ["c1445f3f-090b-4104-98ab-2840cf121f0d"], indirect=True)
    @pytest.mark.parametrize('check_vm_status', ["active"], indirect=True)
    def test_create_vm_net_disk(self, create_vm_net_disk, check_vm_status):
        assert check_vm_status

    @pytest.mark.parametrize('create_vm_local_disk', ["c1445f3f-090b-4104-98ab-2840cf121f0dqwe"], indirect=True)
    @pytest.mark.parametrize('check_vm_status', ["None"], indirect=True)
    def test_negative_vm_local_disk(self, create_vm_local_disk, check_vm_status):
        assert check_vm_status is None

    @pytest.mark.parametrize('create_vm_net_disk', ["c1445f3f-090b-4104-98ab-2840cf121f0dqwe"], indirect=True)
    @pytest.mark.parametrize('check_vm_status', ["None"], indirect=True)
    def test_negative_vm_net_disk(self, create_vm_net_disk, check_vm_status):
        assert check_vm_status is None

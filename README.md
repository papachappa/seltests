Pytest тесты для Selectel


Предварительные шаги: 
Тесты запускаются в системе Ubuntu 20.04
Предварительно должен быть заведен пользователь в системе Selectel

Для установки на локальную систему Ubuntu 20.04 программного обеспечения, необходимого для работы с консольными клиентами OpenStack, используйте следующие команды.

apt update
apt -y install build-essential curl git \
    libffi-dev libssl-dev libxml2-dev libxslt1-dev \
    python3-pip python3-dev python3-openssl python3-pyasn1
pip3 install -UI pbr setuptools pytz
pip3 install -UI git+https://github.com/openstack/python-openstackclient.git@stable/wallaby

Для запуска тестов локально дожен быть установлен клиент openstack(Openstack CLI), а также pytest версии 6.2.5
RC файл должен использоваться, который поставляется в репозитории
Для запуска тестов нужно использоваться команду pytest -s tests.py

Тесты реализуют функционал через клиента Openstack CLI:
- создание виртуальной машины с двумя сетевыми дисками
- создание виртуальной машины с локальным диском
- удаление виртуальной машины
- негативные тесты на невозможность создать виртуальную машину из-за неправильных параметров

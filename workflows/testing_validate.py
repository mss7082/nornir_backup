#!/home/gns3/virtualenvs/nornir/bin/python

from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking, text


def main():
    nr = InitNornir(config_file="../config.yaml")
    devices = nr.filter(F(platform="junos"))
    # import ipdb

    # ipdb.set_trace()
    result = devices.run(task=networking.napalm_validate, src="../validators/validate.yaml",)
    print_result(result)


if __name__ == "__main__":
    main()

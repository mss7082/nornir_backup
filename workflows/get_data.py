#!/home/gns3/virtualenvs/nornir/bin/python

from nornir import InitNornir
from pprint import pprint
from nornir.plugins.tasks import networking, text
from nornir.plugins.functions.text import print_result
from nornir.core.filter import F

import logging


def main():
    nr = InitNornir(config_file="../config.yaml")
    # pprint(nr.inventory.get_inventory_dict()["hosts"])
    juniper = nr.filter(F(platform="junos"))
    result = juniper.run(task=networking.napalm_get, getters=["interfaces_ip"])
    print_result(result)


main()

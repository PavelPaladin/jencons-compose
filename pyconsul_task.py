#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script is designed for:
    - Set key=value for Consul
    - Get key=value from Consul
Example usage for inject:
    $ python3 pyconsul_task.py
.. _Google Python Style Guide:
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__version__ = '1.0'
__author__ = 'Pavel Voytsovich'


import consul


def terraform_inject(service_name, secrets):
    """Rendering  understandable secrets file"""

    with open("te/" + "ololo.", 'w+') as out:
        for secret in filter(params_filter, secrets):
            print("Exporting:", secret['Name'])
        out.write('}\n')

def main():
    """Main function, calling inject by default, or migrate env if specified"""
    shell_args = get_parser()
    service_name = shell_args.service
    prefix = "/%s/%s" % (shell_args.env, shell_args.service)
    terraform_inject(service_name, secrets)


if __name__ == "__main__":
    main()
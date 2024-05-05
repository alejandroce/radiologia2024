#!/usr/bin/env python
import os
import sys
#
# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ludoteca.settings")
#
#     from django.core.management import execute_from_command_line
#
#     execute_from_command_line(sys.argv)


settings = os.environ.get('FILE_SETTINGS')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings." + settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
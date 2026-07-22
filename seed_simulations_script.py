#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nexus_backend.settings')
django.setup()

from curriculum.management.commands.populate_simulations import Command

if __name__ == '__main__':
    cmd = Command()
    cmd.handle()

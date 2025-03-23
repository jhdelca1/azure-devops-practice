#!/bin/bash
ansible-playbook -i hosts playbook.yml --ask-become-pass

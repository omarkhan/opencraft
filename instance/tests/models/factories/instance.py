# -*- coding: utf-8 -*-
#
# OpenCraft -- tools to aid developing and hosting free software projects
# Copyright (C) 2015 OpenCraft <xavier@opencraft.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
OpenEdXInstance model - Factories
"""

# Imports #####################################################################

import factory
from factory.django import DjangoModelFactory

from instance.models.instance import OpenEdXInstance


# Classes #####################################################################

class OpenEdXInstanceFactory(DjangoModelFactory):
    """
    Factory for OpenEdXInstance
    """
    class Meta: #pylint: disable=missing-docstring
        model = OpenEdXInstance

    sub_domain = factory.Sequence('instance{}.test'.format)
    name = factory.Sequence('Test Instance {}'.format)
    commit_id = factory.Sequence('{:>040}'.format)
    github_organization_name = factory.Sequence('test-org{}'.format)
    github_repository_name = factory.Sequence('test-repo{}'.format)

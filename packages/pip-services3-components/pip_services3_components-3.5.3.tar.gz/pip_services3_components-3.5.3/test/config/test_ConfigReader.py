# -*- coding: utf-8 -*-
"""
    tests.config.test_ConfigReader
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""
from pybars import Compiler


class TestConfigReader:
    def test_process_templates(self):
        config = "{{#if A}}{{B}}{{/if}}"
        values = {"A": "true", "B": "XYZ"}

        compiler = Compiler()
        template = compiler.compile(config)

        assert "XYZ" == template(values)

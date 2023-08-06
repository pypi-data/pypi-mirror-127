# -----------------------------------------------------------------------------
# sheng: utils.py
#
# Copyright (c) 2021
# luojiahai
# All rights reserved.
#
# Latest version: https://github.com/luojiahai/sheng
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# BEGIN utils.py
# -----------------------------------------------------------------------------

import sys


class Global(object):

    class __Global(object):

        def __init__(self):
            self._debug = False
            self._debug_lex = False
            self._debug_yacc = False
            self._input_stream = sys.stdin
            self._output_stream = sys.stdout
            self._error_stream = sys.stderr
            self._log_stream = sys.stderr
            self._log = None

        @property
        def debug(self):
            return self._debug

        @debug.setter
        def debug(self, other):
            self._debug = other

        @property
        def debug_lex(self):
            return self._debug_lex

        @debug_lex.setter
        def debug_lex(self, other):
            self._debug_lex = other

        @property
        def debug_yacc(self):
            return self._debug_yacc

        @debug_yacc.setter
        def debug_yacc(self, other):
            self._debug_yacc = other

        @property
        def input_stream(self):
            return self._input_stream

        @input_stream.setter
        def input_stream(self, other):
            self._input_stream = other
            
        @property
        def output_stream(self):
            return self._output_stream

        @output_stream.setter
        def output_stream(self, other):
            self._output_stream = other

        @property
        def error_stream(self):
            return self._error_stream

        @error_stream.setter
        def error_stream(self, other):
            self._error_stream = other

        @property
        def log_stream(self):
            return self._log_stream

        @log_stream.setter
        def log_stream(self, other):
            self._log_stream = other

        @property
        def log(self):
            return self._log

        @log.setter
        def log(self, other):
            self._log = other

    __instance = None

    def __new__(cls):
        if (not Global.__instance):
            Global.__instance = Global.__Global()
        return Global.__instance


# -----------------------------------------------------------------------------
# END utils.py
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# sheng: compile.py
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
# BEGIN compile.py
# -----------------------------------------------------------------------------

import inspect
from sys import stderr
import traceback
from .ply import *
from .lex import *
from .parse import *
from .ast import *
from .context import *
from .builtins import *


def execute(data):
    try:
        # Lex
        lexer = Lexer()
        lexer.build(
            debug=Global().debug_lex, 
            debuglog=Global().log if Global().debug_lex else None
        )
        
        # Initialise context with symbol table
        symtable = SymbolTable()
        context = Context(symtable)

        # Add builtin functions to the symbol table
        def get_default_args(func):
            signature = inspect.signature(func)
            return {
                k: v.default
                for k, v in signature.parameters.items()
                if v.default is not inspect.Parameter.empty
            }
        for identifier, function_pointer in BUILTIN_FUNCTIONS.items():
            name = Name(identifier)
            parameters = [
                Name(arg)
                for arg in inspect.getfullargspec(function_pointer)[0]
            ]
            default_args = get_default_args(function_pointer)
            functiondef = FunctionDef(
                name, parameters, function_pointer, default_args
            )
            context.symtable.insert(identifier, functiondef)

        # Parse
        parser = yacc.yacc(
            debug=Global().debug_yacc, 
            debuglog=Global().log if Global().debug_yacc else None
        )
        ast = parser.parse(data)
        return ast.evaluate(context)
        
    except BaseException as e:
        if (isinstance(e, ShengException)):
            print(e, file=Global().error_stream)
            if (Global().debug):
                Global().log.error(f'{e}')
                Global().log.debug(f'{traceback.format_exc()}')
        else:
            error_message = f'编译器报错（未被捕捉的错误）：{type(e).__name__}\n' \
                '（1）请重新运行命令，在命令中添加\'--debug\'获取运行日志\n' \
                '（2）在\'./log\'文件夹中查看运行日志文件\n' \
                '（3）提交至结绳的GitHub仓库请求修复'
            print(error_message, file=Global().error_stream)
            if (Global().debug):
                Global().log.error(f'{error_message}')
                Global().log.debug(f'{traceback.format_exc()}')

    finally:
        return None


# -----------------------------------------------------------------------------
# ENG compile.py
# -----------------------------------------------------------------------------

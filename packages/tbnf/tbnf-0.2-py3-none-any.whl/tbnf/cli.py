from wisepy2 import wise
import traceback
import sys

show_less = [False]

def format_exceptions(e: Exception):
    if show_less[0]:
        remove_py_traceback(e)
    return ''.join(traceback.format_exception(type(e), e, e.__traceback__))

def remove_py_traceback(e):
    e.__traceback__ = None
    e_cur = e
    while e_cur := e_cur.__cause__:
        e_cur.__traceback__ = None
    return e



def command(
    filename: str, backend: str, outdir: str = ".", mod: str = "mylang", less: bool = False
):
    """
    filename: tbnf grammar
    backend: lark | antlr | csharp
    """
    from tbnf.backends import lark, antlr, csharp, ocaml
    from tbnf import parser as p
    from tbnf.parser_utils import using_source_path, remove_imports
    from tbnf import t, unify, typecheck
    from tbnf.common import refs
    from tbnf.macroresolve import resolve_macro
    from tbnf.beforecodegen import merge_definitions
    import os
    
    show_less[0] = less

    backends = {"lark": lark, "antlr": antlr, 'csharp': csharp, 'ocaml': ocaml}

    with open(filename, encoding="utf8") as f:
        grammar_src = f.read()
    
    with using_source_path(filename):
        stmts = p.parser.parse(grammar_src)
    
    stmts = remove_imports(stmts)
    stmts = resolve_macro(stmts)
    # pprint(stmts)
    tc = typecheck.Check(stmts)
    tc.check_all()
    for each in refs:
        try:
            each.set(p.uf.prune(each.get()))
        except:
            # TODO: unsolved type
            raise
    # print(tc.global_scopes.keys())
    

    cg = backends[backend].CG(tc.global_scopes)
    def out_io(s):
        return open(os.path.join(outdir, s), "w")
    
    stmts = merge_definitions(stmts)
    cg.process(stmts)
    cg.out(mod, out_io)


def main():
    try:
        wise(command)()
    except Exception as e:
        print(format_exceptions(e))
        if not show_less[0]:
            print("(add --less to remove development errors.)")
        sys.exit(1)

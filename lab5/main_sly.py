import sys
from scanner_sly import Scanner
from parser_sly import Mparser
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker
from Interpreter import Interpreter

if __name__ == '__main__':
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "examples/example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    lexer = Scanner()
    parser = Mparser()
    ast = parser.parse(lexer.tokenize(text))

    # Below code shows how to use visitor
    if ast is not None:
        print("Abstract syntax tree:")
        ast.printTree()
        print()
        
        typeChecker = TypeChecker()   
        typeChecker.visit(ast) # or alternatively ast.accept(typeChecker)

        if len(typeChecker.errors) > 0:
            print("Semantic analysis failed! Errors:")

            for error in typeChecker.errors:
                print(error)
        else:
            print("Interpreting the program:")
            interpreter = Interpreter()
            interpreter.visit(ast)
            # in future
            # ast.accept(OptimizationPass1())
            # ast.accept(OptimizationPass2())
            # ast.accept(CodeGenerator())

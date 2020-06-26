from interpreter import Interpreter
from lexer import Lexer
from syntax_analyzer import SyntaxAnalyzer
from semantic_analyzer import SemanticAnalyzer

def main():
    if __name__ == '__main__':
        import sys
        text = open(sys.argv[1], 'r').read()
        lexer = Lexer(text)
        parser = SyntaxAnalyzer(lexer)
        tree = parser.parse()
        semantic_analyzer = SemanticAnalyzer()
        try:
            semantic_analyzer.visit(tree)
        except Exception as e:
            print(e)

    interpreter = Interpreter(tree)
    interpreter.interpret()
    for k, v in sorted(interpreter.GLOBAL_MEMORY.items()):
        print('{} = {}'.format(k, v))


if __name__ == '__main__':
    main()
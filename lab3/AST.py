class Node(object):
    pass

class MultipleStmts(Node):
    def __init__(self, stmts_rec, stmt):
        self.stmts_rec = stmts_rec
        self.stmt = stmt

class SingleStmt(Node):
    def __init__(self, stmt):
        self.stmt = stmt

class ControlStmts(Node):
    def __init__(self, control_statement):
        self.control_statement = control_statement

class StatementsSet(Node):
    def __init__(self, stmts):
        self.stmts = stmts

class SpecificStmt(Node):
    def __init__(self, specific_stmt):
        self.specific_stmt = specific_stmt

class ReturnExpression(Node):
    def __init__(self, expression):
        self.expression = expression

class IfElseStmt(Node):
    def __init__(self, rel_expr, if_stmt, else_stmt):
        self.rel_expr = rel_expr
        self.if_stmt = if_stmt
        self.else_stmt = else_stmt

class IfStmt(Node):
    def __init__(self, rel_expr, if_stmt):
        self.rel_expr = rel_expr
        self.if_stmt = if_stmt

class WhileStmt(Node):
    def __init__(self, rel_expr, while_stmt):
        self.rel_expr = rel_expr
        self.while_stmt = while_stmt

class ForStmt(Node):
    def __init__(self, iter_variable, range_begin, range_end, for_stmt):
        self.iter_variable = iter_variable
        self.range_begin = range_begin
        self.range_end = range_end
        self.for_stmt = for_stmt

class PrintStmt(Node):
    def __init__(self, print_stmt):
        self.print_stmt = print_stmt

class PrintRecursive(Node):
    def __init__(self, print_rec, val):
        self.print_rec = print_rec
        self.val = val

class Value(Node):
    def __init__(self, val):
        self.val = val

class Variable(Node):
    def __init__(self, name):
        self.name = name

class IntNum(Node):
    def __init__(self, value):
        self.value = value

class AssignExpression(Node):
    def __init__(self, expression):
        self.expression = expression

class RelationExpression(Node):
    def __init__(self, expression):
        self.expression = expression

class MatrixExpression(Node):
    def __init__(self, expression):
        self.expression = expression

class UnaryExpression(Node):
    def __init__(self, op, expression):
        self.op = op
        self.expression = expression

class MatrixRows(Node):
    def __init__(self, rows):
        self.rows = rows

class NumLine(Node):
    def __init__(self, num_line):
        self.num_line = num_line

class GeneralExpression(Node):
    def __init__(self, expression):
        self.expression = expression

class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class MatrixRef(Node):
    def __init__(self, matrix_ref):
        self.matrix_ref = matrix_ref

class TabRef(Node):
    def __init__(self, tab_ref):
        self.tab_ref = tab_ref

class DoubleRef(Node):
    def __init__(self, id, row, col):
        self.id = id
        self.row = row
        self.col = col

class SingleRef(Node):
    def __init__(self, id, row):
        self.id = id
        self.row = row

class TabRefBoth(Node):
    def __init__(self, id, begin, end):
        self.id = id
        self.begin = begin
        self.end = end

class TabRefEnd(Node):
    def __init__(self, id, end):
        self.id = id
        self.end = end

class TabRefBegin(Node):
    def __init__(self, id, begin):
        self.id = id
        self.begin = begin

class MatrixRowRec(Node):
    def __init__(self, matrix_rows, num_line):
        self.matrix_rows = matrix_rows
        self.num_line = num_line
    
class NumLineRec(Node):
    def __init__(self, num_line, val):
        self.num_line = num_line
        self.val = val

class MatrixFuncs(Node):
    def __init__(self, fun, value):
        self.fun = fun
        self.value = value

class FloatNum(Node):
    def __init__(self, value):
        self.value = value

class String(Node):
    def __init__(self, value):
        self.value = value

class Error(Node):
    def __init__(self):
        pass

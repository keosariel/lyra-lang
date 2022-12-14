from llvmlite import ir


class LyraBaseType:
    llvm_base_type = None
    llvm_type = None

class LyraIntType(LyraBaseType):

    llvm_base_type = ir.IntType
    llvm_type = None

    def __init__(self, bits=64, signed=True):
        self.bits = bits
        self.signed = signed
        self.llvm_type = self.llvm_base_type(bits)

    def str_rep(self):
        rep = "i" if self.signed else "u"
        return f"{rep}{self.bits}"

    def as_pointer(self):
        return self.llvm_type.as_pointer()

    def __repr__(self):
        rep = "i" if self.signed else "u"
        return f"<{self.__class__.__name__} ({rep}{self.bits})>"

class LyraBoolType(LyraIntType):

    def __init__(self):
        super().__init__(bits=1, signed=False)

    def str_rep(self):
        return "bool"

    def as_pointer(self):
        return self.llvm_type.as_pointer()

class LyraFloatType(LyraBaseType):

    llvm_base_type = ir.FloatType
    llvm_type = llvm_base_type()

    def as_pointer(self):
        return self.llvm_type.as_pointer()

    def str_rep(self):
        return "f32"

    def __repr__(self):
        return f"<{self.__class__.__name__} (f32)>"


class LyraDoubleType(LyraBaseType):

    llvm_base_type = ir.DoubleType
    llvm_type = llvm_base_type()


    def as_pointer(self):
        return self.llvm_type.as_pointer()

    def str_rep(self):
        return "f64"

    def __repr__(self):
        return f"<{self.__class__.__name__} (f64)>"

class LyraVoidType(LyraBaseType):

    llvm_base_type = ir.VoidType
    llvm_type = llvm_base_type()

    def as_pointer(self):
        return self.llvm_type.as_pointer()
    
    def str_rep(self):
        return "void"

    def __repr__(self):
        return f"<{self.__class__.__name__} (void)>"

class LyraFunctionType:

    llvm_base_type = ir.FunctionType
    llvm_type = None

    def __init__(self, ret, *args):
        """
        Instantiates a New llvm function type

        Args:
            ret (LyraBaseType): function return type
            args (List[LyraBaseType]): list of the function parameters
        """


        v_error = ValueError(f"Expected an instance of LyraBaseType")

        for i, typ in enumerate(args):
            if not isinstance(typ, LyraBaseType):
                raise v_error

        if not isinstance(ret, LyraBaseType):
            raise v_error

        self.args = args
        self.return_type = ret

    def str_rep(self):
        return f"function({','.join([x.str_rep() for x in self.args])}):{self.return_type.str_rep()}"

    def __repr__(self):
        return f"<{self.__class__.__name__} (function({self.args})->{self.return_type})>"




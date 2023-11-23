from securify.solidity import solidity_ast_compiler, solidity_cfg_compiler
from securify.staticanalysis.visualization import visualize
from securify.staticanalysis.factencoder import encode
from securify.analyses.analysis import AnalysisConfiguration, AnalysisContext

# ast = solidity_ast_compiler.compile_ast("./test.sol")

# cfg = solidity_cfg_compiler.compile_cfg(ast)

config = AnalysisConfiguration(
        # TODO: this returns only the dict ast, but should return the object representation
        ast_compiler=lambda t: solidity_ast_compiler.compile_ast(t.source_file),
        cfg_compiler=lambda t: solidity_cfg_compiler.compile_cfg(t.ast).cfg,
        static_analysis=lambda t: None
    )

context = AnalysisContext(
        config=config,
        source_file="./test.sol"
    )
# print(cfg)

facts, _ = encode(context.cfg)
print(context.cfg)
print(facts)
visualize(facts).render("out/dl", format="svg", cleanup=True)
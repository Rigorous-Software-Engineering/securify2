import json
from securify.solidity import solidity_ast_compiler, solidity_cfg_compiler
from securify.staticanalysis.static_analysis import StaticAnalysisResult
from securify.staticanalysis.visualization import visualize
from securify.staticanalysis.factencoder import encode
from securify.analyses.analysis import AnalysisConfiguration, AnalysisContext
from sys import argv

if len(argv) < 2:
    print("Missing argument: contract path")
    exit()

contract = argv[1]
contract_name = contract.replace(".sol", "")

config = AnalysisConfiguration(
        # TODO: this returns only the dict ast, but should return the object representation
        ast_compiler=lambda t: solidity_ast_compiler.compile_ast(t.source_file),
        cfg_compiler=lambda t: solidity_cfg_compiler.compile_cfg(t.ast).cfg,
        static_analysis=lambda t: StaticAnalysisResult([], {}, {}, "", "", 0)
    )

context = AnalysisContext(
        config=config,
        source_file=contract
    )

ast = context.ast

with open(contract_name + ".ast", "w") as outfile:
    version = ast["_solc_version"]# getattr(ast, "_solc_version")
    ast["_solc_version"] = str(version)
    json.dump(ast, outfile)

facts, _ = encode(context.cfg)
print(context.cfg)
visualize(facts).render("out/dl", format="svg", cleanup=True)
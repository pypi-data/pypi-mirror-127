import json
from LTO import PyCLTO
from LTOCli import handle_default as handle
import sys

def func(name_space, parser):
    chain_id = handle.check(name_space.network[0], parser) if name_space.network else 'L'
    account_name = vars(name_space)['account'][0] if vars(name_space)['account'] else ''
    txJson = name_space.stdin.read() if not sys.stdin.isatty() else ""
    if not json:
        parser.error("Expected transaction as input, type 'lto broadcast --help' for instructions")

    transaction = PyCLTO().from_data(json.loads(txJson))

    if vars(name_space)['unsigned'] is False:
        if not transaction.proofs:
            transaction.sign_with(handle.get_account(chain_id, parser, account_name))
        if vars(name_space)['no_broadcast'] is False:
            transaction = transaction.broadcast_to(handle.get_node(chain_id, parser))
    else:
        if not transaction.proofs:
            parser.error("Transaction needs to be signed before broadcasting, type 'lto broadcast --help' for instruction")
        else:
            if vars(name_space)['no_broadcast'] is False:
                transaction = transaction.broadcast_to(handle.get_node(chain_id, parser))

    handle.pretty_print(transaction)



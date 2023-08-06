from LTOCli import handle_default as handle
from LTO.Transactions.sponsorship import Sponsorship
from LTO.Transactions.cancel_sponsorship import CancelSponsorship


def func(name_space,parser):
    if vars(name_space)['subparser-name-sponsorship']:
        chain_id = handle.check(name_space.network[0], parser) if name_space.network else 'L'
        account_name = vars(name_space)['account'][0] if vars(name_space)['account'] else ''
        sponsor = vars(name_space)['sponsor'][0] if vars(name_space)['sponsor'] else None

    if vars(name_space)['subparser-name-sponsorship'] == 'create':
        transaction = Sponsorship(name_space.recipient[0])
        if vars(name_space)['unsigned'] is False:
            transaction.sign_with(handle.get_account(chain_id, parser, account_name))
            if sponsor:
                transaction.sponsor_with(handle.get_account(chain_id, parser, sponsor))
            if vars(name_space)['no_broadcast'] is False:
                transaction = transaction.broadcast_to(handle.get_node(chain_id, parser))
        elif vars(name_space)['no_broadcast'] is False:
            parser.error(
                "Use the '--unsigned' option only in combination with the '--no-broadcast' option. Type 'lto sponsorship create --help' for more informations ")
        handle.pretty_print(transaction)

    elif vars(name_space)['subparser-name-sponsorship'] == 'cancel':
        transaction = CancelSponsorship(name_space.recipient[0])
        if vars(name_space)['unsigned'] is False:
            transaction.sign_with(handle.get_account(chain_id, parser, account_name))
            if sponsor:
                transaction.sponsor_with(handle.get_account(chain_id, parser, sponsor))
            if vars(name_space)['no_broadcast'] is False:
                transaction = transaction.broadcast_to(handle.get_node(chain_id, parser))
        elif vars(name_space)['no_broadcast'] is False:
            parser.error(
                "Use the '--unsigned' option only in combination with the '--no-broadcast' option. Type 'lto sponsorship cancel --help' for more informations ")
        handle.pretty_print(transaction)

    elif vars(name_space)['subparser-name-sponsorship'] == 'list':
        pass

    elif vars(name_space)['subparser-name-sponsorship'] == 'list-inbound':
        node = handle.get_node(chain_id, parser)
        address = handle.get_account(chain_id, parser, account_name).address
        value = node.sponsorshipList(address)
        if value['sponsor']:
            for x in value['sponsor']:
                print(x)
        else:
            print('No inbound sponsorships found')

    else:
        parser.error('Type lto sponsorship --help for instructions')




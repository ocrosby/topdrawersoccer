from pytest_bdd import when

from topdrawersoccer.extractors.transfer_extractor import TransferExtractor

extractor = TransferExtractor()


@when('I retrieve the list of transfer colleges')
def retrieve_list_of_transfer_colleges(context):
    college_names = None

    try:
        college_names = extractor.get_transfer_colleges()
    except Exception as e:
        context['errors'].append(str(e))
    finally:
        context['list'] = college_names


@when('I retrieve a list of outgoing transfer colleges')
def retrieve_list_of_outgoing_transfer_colleges(context):
    college_names = None

    try:
        college_names = extractor.get_outgoing_transfer_colleges()
    except Exception as e:
        context['errors'].append(str(e))
    finally:
        context['list'] = college_names


@when('I retrieve a list of incoming transfer colleges')
def retrieve_list_of_incoming_transfer_colleges(context):
    college_names = None

    try:
        college_names = extractor.get_incoming_transfer_colleges()
    except Exception as e:
        context['errors'].append(str(e))
    finally:
        context['list'] = college_names


@when('I retrieve the list of transfer players')
def retrieve_list_of_transfer_players(context):
    transfers = None

    try:
        transfers = extractor.get_transfer_players()
    except Exception as e:
        context['errors'].append(str(e))
    finally:
        context['list'] = transfers



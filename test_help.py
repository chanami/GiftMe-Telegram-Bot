import help
import settings
def test_help():
    new_help = help.Help()
    assert new_help.get_explanation('/add_event') == 'Adding an event and linked to existing friend'

def main(args):
    try:
        print("\nAttempting to force pull remote todo list...", end = ' ')
        # backup current list
        # delete current list
        # curl down old
        # assert valid
        print("Success.")
    except Exception as e:
        print(f'Failure! restoring current todo list:\n{e}')

import logging
logger = logging.getLogger(__name__)
from ..utils import range_to_str, yprint, run_routine


def show_routine(args):
    try:
        from ..db import load_routine, list_routine
    except Exception as e:
        logger.error(e)
        return

    # List routines
    if args.routine_name is None:
        routines = list_routine()[0]
        if routines:
            yprint(routines)
        else:
            print('No routine has been saved yet')
        return

    try:
        routine, _ = load_routine(args.routine_name)
        if routine is None:
            print(f'Routine {args.routine_name} not found')
            return
    except Exception as e:
        print(e)
        return

    # Print the routine
    if not args.run:
        routine['config']['variables'] = range_to_str(routine['config']['variables'])
        yprint(routine)
        return

    # Run the routine
    try:
        run_routine(routine, args.yes, None, args.verbose)
    except Exception as e:
        logger.error(e)

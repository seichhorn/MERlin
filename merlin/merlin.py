import argparse
import cProfile
import dotenv

from merlin.core import dataset
from merlin.core import scheduler

def build_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--profile', action='store_true', 
            help='enable profiling')

    parser.add_argument('-d', '--data-set', required=True)
    parser.add_argument('-o', '--data-organization')
    parser.add_argument('-c', '--codebook')
    parser.add_argument('-a', '--analysis-parameters')

    return parser


def merlin():
    print('MERlin - MERFISH decoding software')
    parser = build_parser()
    args, argv = parser.parse_known_args()
    dotenv.load_dotenv(dotenv.find_dotenv())

    if args.profile:
        profiler = cProfile.Profile()
        profiler.enable()

    dataSet = dataset.MERFISHDataSet(args.data_set, 
            dataOrganizationName=args.data_organization,
            codebookName=args.codebook)

    parametersHome = os.environ.get('PARAMETERS_HOME')
    with open(args.analysis_parameters, 'r') as f:
        s = scheduler.Scheduler(
                dataSet, json.load(os.sep.join([parametersHome, f])))

    s.run()


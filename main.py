from blockmirror.monitor import BlockMirror
import argparse

parser = argparse.ArgumentParser(description="Blockchain confirmation time monitor")
parser.add_argument('--chains', nargs='+', default=['btc', 'eth'], help='Chains to monitor (e.g., btc eth)')
parser.add_argument('--interval', type=int, default=60, help='Update interval in seconds')

args = parser.parse_args()

bm = BlockMirror(args.chains, args.interval)
bm.run()

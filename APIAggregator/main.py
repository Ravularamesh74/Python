from aggregator import aggregate_data
from utils import pretty_print

def main():
    data = aggregate_data()
    pretty_print(data)

if __name__ == "__main__":
    main()
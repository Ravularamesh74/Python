from datetime import datetime

def pretty_print(data):
    print("\n📊 Aggregated Report")
    print("----------------------")
    print(f"Time: {datetime.now()}\n")

    for key, value in data.items():
        print(f"{key.upper()}:")
        for k, v in value.items():
            print(f"  {k}: {v}")
        print()
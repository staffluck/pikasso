import csv


def main():
    file_path = "police_data.csv"
    with open(file_path, "r", newline="") as f:
        reader = csv.reader(f, delimiter=",", quotechar="|")
        for row in reader:
            pass

if __name__ == "__main__":
    main()
 
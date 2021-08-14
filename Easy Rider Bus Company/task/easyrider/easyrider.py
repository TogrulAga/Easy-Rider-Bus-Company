import json
import re


class BusCompany:
    def __init__(self):
        self.data = None
        self.type_error_counts = dict()
        self.format_error_counts = dict()
        self.bus_stop_counts = dict()
        self.bus_lines = dict()
        self.bus_stop_names = dict()
        self.get_data()
        self.check_bus_lines()
        self.check_on_demand_stops()

    def get_data(self):
        self.data = json.loads(input())

    def count_type_errors(self):
        self.type_error_counts.setdefault("bus_id", 0)
        self.type_error_counts.setdefault("stop_id", 0)
        self.type_error_counts.setdefault("stop_name", 0)
        self.type_error_counts.setdefault("next_stop", 0)
        self.type_error_counts.setdefault("stop_type", 0)
        self.type_error_counts.setdefault("a_time", 0)

        for line in self.data:
            if not isinstance(line["bus_id"], int):
                self.type_error_counts["bus_id"] += 1
            if not isinstance(line["stop_id"], int):
                self.type_error_counts["stop_id"] += 1
            if not isinstance(line["next_stop"], int):
                self.type_error_counts["next_stop"] += 1
            if line["stop_name"] == "" or not isinstance(line["stop_name"], str):
                self.type_error_counts["stop_name"] += 1
            if not isinstance(line["stop_type"], str) or (len(line["stop_type"]) > 0 and line["stop_type"] not in "SOF"):
                self.type_error_counts["stop_type"] += 1
            if line["a_time"] == "" or not isinstance(line["a_time"], str):
                self.type_error_counts["a_time"] += 1

    def type_validation_summary(self):
        print(f"Type and required field validation: {sum(self.type_error_counts.values())}")
        for key, value in self.type_error_counts.items():
            print(f"{key}: {value}")

    def count_format_errors(self):
        self.format_error_counts.setdefault("stop_name", 0)
        self.format_error_counts.setdefault("stop_type", 0)
        self.format_error_counts.setdefault("a_time", 0)

        for line in self.data:
            if not re.search(r"(?<=[A-Z])[a-zA-Z ]+ (?=(Road|Avenue|Boulevard|Street)$)", line["stop_name"]):
                self.format_error_counts["stop_name"] += 1
            if not re.match(r"([SOF]$)+|$", line["stop_type"]):
                self.format_error_counts["stop_type"] += 1
            if not re.match(r"([0-1][0-9]|2[0-3]):([0-5][0-9])$", line["a_time"]):
                self.format_error_counts["a_time"] += 1

    def format_validation_summary(self):
        print(f"Format validation: {sum(self.format_error_counts.values())}")

        for key, value in self.format_error_counts.items():
            print(f"{key}: {value}")

    def count_stops(self):
        for line in self.data:
            self.bus_stop_counts.setdefault(line["bus_id"], 0)
            self.bus_stop_counts[line["bus_id"]] += 1

    def stops_summary(self):
        print("Line names and number of stops:")
        for bus_id, stops in self.bus_stop_counts.items():
            print(f"bus_id: {bus_id}, stops: {stops}")

    def check_bus_lines(self):
        self.bus_stop_names.setdefault("S", [])
        self.bus_stop_names.setdefault("T", [])
        self.bus_stop_names.setdefault("F", [])

        for line in self.data:
            self.bus_lines.setdefault(line["bus_id"], {"S": None, "F": None, "all": []})
            if line["stop_type"] in "SF" and line["stop_type"] != "":
                self.bus_lines[line["bus_id"]][line["stop_type"]] = line["stop_name"]
                if line["stop_name"] not in self.bus_stop_names[line["stop_type"]]:
                    self.bus_stop_names[line["stop_type"]].append(line["stop_name"])

            self.bus_lines[line["bus_id"]]["all"].append(line["stop_name"])

        for line1, stops1 in self.bus_lines.items():
            for line2, stops2 in self.bus_lines.items():
                if line1 != line2:
                    intersection = set.intersection(set(stops1["all"]), set(stops2["all"]))
                    if intersection is not set():
                        self.bus_stop_names["T"].extend(list(intersection))

        self.bus_stop_names["T"] = list(set(self.bus_stop_names["T"]))

    def bus_lines_summary(self):
        for bus_id, start_finish in self.bus_lines.items():
            if start_finish["S"] is None or start_finish["F"] is None:
                print(f"There is no start or end stop for the line: {bus_id}")
                return

        print(f"Start stops: {len(self.bus_stop_names['S'])} {sorted(self.bus_stop_names['S'])}")
        print(f"Transfer stops: {len(self.bus_stop_names['T'])} {sorted(self.bus_stop_names['T'])}")
        print(f"Finish stops: {len(self.bus_stop_names['F'])} {sorted(self.bus_stop_names['F'])}")

    def check_arrival_times(self):
        print("Arrival time test:")
        lines = dict()
        for line in self.data:
            lines.setdefault(line["bus_id"], [])
            lines[line["bus_id"]].append(line)

        aok = True
        for bus_id, line in lines.items():
            previous_time = "00:00"
            for i in line:
                if previous_time > i["a_time"]:
                    print(f"bus_id line {bus_id}: wrong time on station {i['stop_name']}")
                    aok = False
                    break
                previous_time = i["a_time"]

        if aok:
            print("OK")

    def check_on_demand_stops(self):
        wrong_on_demand = []
        for line in self.data:
            if line["stop_name"] in self.bus_stop_names["T"] and line["stop_type"] == "O":
                wrong_on_demand.append(line["stop_name"])

        print("On demand stops test:")
        if wrong_on_demand:
            print(f"Wrong stop type: {sorted(wrong_on_demand)}")
        else:
            print("OK")


_ = BusCompany()

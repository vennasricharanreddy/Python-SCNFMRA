# ================= IMPORTS =================
from scnfmra.models.map_node import MapNode
from scnfmra.utils.navigation_utils import bfs

from scnfmra.models.facility import Facility
from scnfmra.models.booking import Booking
from scnfmra.models.complaint import Complaint
from scnfmra.models.asset import Asset

from scnfmra.utils.id_generator import generate_id
from scnfmra.utils.validators import validate_capacity
from scnfmra.utils.exceptions import SchedulingConflictError

from scnfmra.analysis.facility_usage import usage_analysis
from scnfmra.analysis.maintenance_trends import complaint_analysis
from scnfmra.analysis.navigation_analyzer import distance_matrix

from scnfmra.visual.charts import bar_chart, line_chart, pie_chart

# ================= DATA STORAGE =================
facilities = []
bookings = []
complaints = []
assets = []


# ================= NAVIGATION DEMO =================
def navigation_demo():
    print("\n--- CAMPUS NAVIGATION ---")

    A = MapNode("Gate", (0, 0))
    B = MapNode("E-Block", (10, 10))
    C = MapNode("Library", (20, 20))

    A.add_neighbor(B)
    B.add_neighbor(C)

    path = bfs(A, C)

    print("Navigation Path:", [node.node_id for node in path])


# ================= FACILITY =================
def add_facility():
    building = input("Building: ")
    room_type = input("Type: ")
    capacity = int(input("Capacity: "))
    floor = int(input("Floor: "))
    x = int(input("X: "))
    y = int(input("Y: "))

    validate_capacity(capacity)

    fid = generate_id("F")
    facilities.append(Facility(fid, building, room_type, capacity, floor, (x, y)))
    print("Facility Added:", fid)


def view_facilities():
    print("\n--- FACILITIES ---")
    for f in facilities:
        print(f.display())


# ================= BOOKING =================
def book_facility():
    fid = input("Facility ID: ")
    purpose = input("Purpose: ")
    start = input("Start (YYYY-MM-DD HH:MM): ")
    end = input("End (YYYY-MM-DD HH:MM): ")

    new_booking = Booking(fid, purpose, start, end)

    for b in bookings:
        if new_booking.conflicts(b):
            raise SchedulingConflictError("Time conflict!")

    bookings.append(new_booking)
    print("Booking confirmed")


# ================= COMPLAINT =================
def raise_complaint():
    fid = input("Facility ID: ")
    issue = input("Issue: ")
    severity = int(input("Severity (1-5): "))

    cid = generate_id("C")
    complaints.append(Complaint(cid, fid, issue, severity))
    print("Complaint Registered:", cid)


# ================= ASSET =================
def add_asset():
    category = input("Category: ")
    building = input("Building: ")
    room = input("Room: ")
    warranty = input("Warranty Expiry: ")

    aid = generate_id("A")
    assets.append(Asset(aid, category, building, room, warranty))
    print("Asset Added:", aid)


# ================= ANALYTICS =================
def analytics():
    print("\n--- ANALYTICS DASHBOARD ---")

    # ===== FACILITY USAGE =====
    if bookings:
        data = usage_analysis(bookings)

        if data is not None and not data.empty:
            print("\nFacility Usage:")
            print(data)

            try:
                bar_chart(data)
                line_chart(data)
                pie_chart(data)
            except Exception as e:
                print("Chart Error:", e)
        else:
            print("No usable booking data")
    else:
        print("No booking data available")

    # ===== COMPLAINT ANALYSIS =====
    if complaints:
        try:
            comp_data = complaint_analysis(complaints)
            print("\nComplaint Trends:")
            print(comp_data)
        except Exception as e:
            print("Complaint analysis error:", e)
    else:
        print("No complaint data available")

    # ===== NUMPY DISTANCE MATRIX =====
    if facilities:
        try:
            coords = [f.coordinates for f in facilities]
            print("\nDistance Matrix:")
            print(distance_matrix(coords))
        except Exception as e:
            print("Distance calculation error:", e)
    else:
        print("No facility data available")
# ================= MAIN MENU =================
def menu():
    while True:
        print("""
1. Navigation Demo
2. Add Facility
3. View Facilities
4. Book Facility
5. Raise Complaint
6. Add Asset
7. Analytics
8. Exit
9. Load Demo Data
""")

        ch = input("Choice: ")

        if ch == "1":
            navigation_demo()
        elif ch == "2":
            add_facility()
        elif ch == "3":
            view_facilities()
        elif ch == "4":
            try:
                book_facility()
            except Exception as e:
                print(e)
        elif ch == "5":
            raise_complaint()
        elif ch == "6":
            add_asset()
        elif ch == "7":
            analytics()
        elif ch == "9":
            load_demo_data()
        else:
            break


# ================= RUN =================
if __name__ == "__main__":
    def load_demo_data():
        from scnfmra.models.facility import Facility
        from scnfmra.models.booking import Booking
        from scnfmra.models.complaint import Complaint
        from scnfmra.models.asset import Asset

        global facilities, bookings, complaints, assets

        # ===== FACILITIES =====
        facilities.extend([
            Facility("F1001", "E-Block", "Classroom", 60, 2, (10, 20)),
            Facility("F1002", "E-Block", "Lab", 40, 1, (12, 22)),
            Facility("F1003", "Library", "Study Room", 30, 1, (5, 10)),
            Facility("F1004", "Admin Block", "Conference Hall", 100, 3, (20, 30)),
            Facility("F1005", "Mechanical", "Workshop", 80, 1, (25, 35)),
        ])

        # ===== BOOKINGS =====
        bookings.extend([
            Booking("F1001", "Lecture", "2025-08-01 10:00", "2025-08-01 12:00"),
            Booking("F1001", "Seminar", "2025-08-02 09:00", "2025-08-02 11:00"),
            Booking("F1002", "Lab Session", "2025-08-01 11:00", "2025-08-01 01:00"),
            Booking("F1003", "Study Group", "2025-08-03 02:00", "2025-08-03 04:00"),
            Booking("F1004", "Meeting", "2025-08-01 03:00", "2025-08-01 05:00"),
            Booking("F1004", "Workshop", "2025-08-02 01:00", "2025-08-02 04:00"),
        ])

        # ===== COMPLAINTS =====
        complaints.extend([
            Complaint("C1001", "F1001", "Projector issue", 4),
            Complaint("C1002", "F1002", "AC not working", 5),
            Complaint("C1003", "F1003", "Light problem", 2),
            Complaint("C1004", "F1001", "Bench damage", 3),
            Complaint("C1005", "F1004", "Sound system issue", 4),
        ])

        # ===== ASSETS =====
        assets.extend([
            Asset("A1001", "Projector", "E-Block", "E-202", "2026-12-01"),
            Asset("A1002", "Computer", "Lab Block", "L-101", "2025-10-15"),
            Asset("A1003", "AC Unit", "Admin Block", "A-305", "2027-03-20"),
            Asset("A1004", "Printer", "Library", "L-201", "2026-06-10"),
        ])

        print("✅ Rich demo data loaded successfully!")
    menu()
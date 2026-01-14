course = {}
prerequisite = {}

# ------------------ Course Operations ------------------

def addCourse(courseId, name):
    if courseId in course:
        print("Course already exists")
        return
    course[courseId] = name
    print(f"{name} Course Added.")

def removeCourse(courseId):
    if courseId not in course:
        print(f"{courseId} not found")
        return

    print(f"{course[courseId]} Course Removed")
    course.pop(courseId)

    # Remove from prerequisite lists
    prerequisite.pop(courseId, None)
    for c in prerequisite:
        prerequisite[c].discard(courseId)

# ------------------ Prerequisite Logic ------------------

def addPrerequisite(courseId, pres):
    if courseId not in course:
        print(f"{courseId} not found")
        return

    prerequisite.setdefault(courseId, set())

    for pre in pres:
        if pre not in course:
            print(f"{pre} not found")
            continue

        if pre == courseId:
            print("A course cannot be its own prerequisite")
            continue

        if createsCycle(courseId, pre):
            print(f"Adding {pre} creates a cycle. Skipped.")
            continue

        prerequisite[courseId].add(pre)
        print(f"{pre} added as prerequisite for {courseId}")

def createsCycle(courseId, pre):
    visited = set()

    def dfs(node):
        if node == courseId:
            return True
        if node in visited:
            return False
        visited.add(node)
        for p in prerequisite.get(node, []):
            if dfs(p):
                return True
        return False

    return dfs(pre)

# ------------------ Queries ------------------

def listPrerequisite(courseId):
    if courseId not in course:
        print(f"{courseId} not found")
        return

    result = set()

    def dfs(node):
        for p in prerequisite.get(node, []):
            if p not in result:
                result.add(p)
                dfs(p)

    dfs(courseId)

    if result:
        print("Prerequisites:", list(result))
    else:
        print(f"{courseId} requires no prerequisites")

def canEnroll(courseId, completedCourses):
    if courseId not in course:
        print(f"{courseId} not found")
        return

    required = set()

    def dfs(node):
        for p in prerequisite.get(node, []):
            if p not in required:
                required.add(p)
                dfs(p)

    dfs(courseId)

    if required.issubset(set(completedCourses)):
        print("Eligible to enroll")
    else:
        print("Not eligible to enroll")

# ------------------ Menu ------------------

while True:
    print("\n===== Course Management Menu =====")
    print("1. Add a Course")
    print("2. Add Prerequisite for a Course")
    print("3. Remove a Course")
    print("4. List all Prerequisites for a Course")
    print("5. Eligibility check to apply for a Course")
    print("6. Stop")

    ch = int(input("\nEnter choice: "))

    if ch == 1:
        addCourse(input("Enter Course Id: "), input("Enter Course Name: "))

    elif ch == 2:
        addPrerequisite(
            input("Enter Course Id: "),
            input("Enter Prerequisite Id(s): ").split()
        )

    elif ch == 3:
        removeCourse(input("Enter Course Id: "))

    elif ch == 4:
        listPrerequisite(input("Enter Course Id: "))

    elif ch == 5:
        canEnroll(
            input("Enter Course Id: "),
            input("Enter Completed Courses Id(s): ").split()
        )

    elif ch == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice")

    z= input("\nPress Enter to Continue...")
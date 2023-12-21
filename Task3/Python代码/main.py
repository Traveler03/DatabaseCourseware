from DAO import *
from factory import *
from Database import *

def test_dao_factory():
    db = Database('127.0.0.1', 'GardenPlants', 'sa', '123456')

    # 创建 DAOFactory 实例，并传入数据库连接对象
    dao_factory = DAOFactory(db)

    # 创建 CourseDAO 实例并测试其功能
    course_dao = dao_factory.create_course_dao()

    # 创建一个课程对象
    course = Course("C001", "Math", 3, 4, "John Doe")

    # 测试插入功能
    course_dao.insert(course)

    # 测试查找功能
    found_course = course_dao.find("C001")
    print(found_course.get_name())  # 输出: Math

    # 测试更新功能
    course.set_name("Mathematics")
    course_dao.update(course)

    updated_course = course_dao.find("C001")
    print(updated_course.get_name())  # 输出: Mathematics

    # 测试删除功能
    course_dao.delete(course)
    deleted_course = course_dao.find("C001")
    print(deleted_course)  # 输出: None

    # 创建 HomeworkDAO 实例并测试其功能
    homework_dao = dao_factory.create_homework_dao()

    # 创建一个作业对象
    homework = Homework("C001", "S001", 90, 85, 95)

    # 测试插入功能
    homework_dao.insert(homework)

    # 测试更新功能
    homework.set_score1(95)
    homework_dao.update(homework)

    updated_homework = homework_dao.find("C001", "S001")
    print(updated_homework.get_score1())  # 输出: 95

    # 测试删除功能
    homework_dao.delete(homework)
    deleted_homework = homework_dao.find("C001", "S001")
    print(deleted_homework)  # 输出: None

    # 创建 StudentDAO 实例并测试其功能
    student_dao = dao_factory.create_student_dao()

    # 创建一个学生对象
    student = Student("S001", "John Doe", "Male", "Class A", "2000-01-01", "1234567890")

    # 测试插入功能
    student_dao.insert(student)

    # 测试更新功能
    student.set_name("Jane Doe")
    student_dao.update(student)

    updated_student = student_dao.find("S001")
    print(updated_student.get_name())  # 输出: Jane Doe

    # 测试删除功能
    student_dao.delete(student)
    deleted_student = student_dao.find("S001")
    print(deleted_student)  # 输出: None


# 调用测试函数
test_dao_factory()

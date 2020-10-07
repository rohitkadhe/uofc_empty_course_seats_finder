from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from config import DRIVER as driver, WAIT as wait, SCHEDULE_BUILDER_URL
import os
import strings


def open_schedule_builder_page():
    driver.maximize_window()
    driver.get(SCHEDULE_BUILDER_URL)
    continue_button = driver.find_element_by_xpath(
        strings.continue_btn_xpath).click()


def select_term(term):
    wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, strings.semester_terms_class_name)))

    semester_terms = driver.find_elements_by_class_name(strings.semester_terms_class_name)

    for sem_term_element in semester_terms:
        sem_term = sem_term_element.find_element_by_tag_name(
            strings.span).get_attribute(strings.inner_html)

        if(sem_term == term):
            wait.until(EC.element_to_be_clickable((By.NAME, strings.radio_btn_input_name)))
            radio_btn = sem_term_element.find_element_by_name(strings.radio_btn_input_name).click()


def find_course(course_name):
    inp = wait.until(EC.element_to_be_clickable((By.ID, strings.course_search_input_id)))
    inp.send_keys(course_name)
    inp.send_keys(Keys.ENTER)


def course_has_empty_seats():
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, strings.course_table_class_name)))

    lecture_sections = driver.find_elements_by_class_name(strings.lecture_sections_class_name)

    for section in lecture_sections:
        seats_remaining_spans = section.find_elements_by_class_name(strings.seats_class_name)

        if len(seats_remaining_spans) == 0:
            seats_remaining_spans = section.find_elements_by_class_name(strings.seats_full_class_name)

        for seat_remaining_span in seats_remaining_spans:
            if(seat_remaining_span.get_attribute(strings.inner_html) == strings.seats_full):
                return False
    return True


def removeCourse():
    remove_course_btn = driver.find_element_by_xpath(strings.remove_course_btn_xpath).click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, strings.remove_course_btn_xpath)))


def get_courses_from_file():
    courses_file = open(strings.courses_file)
    next(courses_file)
    courses = []

    for course_data in courses_file:
        data = course_data.split(",")
        cd = (data[0], data[1].strip())
        courses.append(cd)

    courses_file.close()
    return courses


def report_if_empty_seats_found(courses):
    results = open(strings.results_file, "w")
    prev_term = ""
    for course_data in courses:
        if(course_data[1] != prev_term):
            select_term(course_data[1])
            prev_term = course_data[1]

        find_course(course_data[0])

        if(course_has_empty_seats()):
            results.write("Course {} has seats\n".format(course_data))
        else:
            results.write("Course {} is full\n".format(course_data))
        removeCourse()

    results.close()
    os.startfile(strings.results_file)


open_schedule_builder_page()
courses = get_courses_from_file()

report_if_empty_seats_found(courses)
driver.close()

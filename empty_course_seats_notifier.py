
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from config import DRIVER as driver, WAIT as wait, TWO_MINS, SCHEDULE_BUILDER_URL


def open_schedule_builder_page():
    driver.maximize_window()
    driver.get(SCHEDULE_BUILDER_URL)
    continue_button = driver.find_element_by_xpath(
        "//div[5]/div/div[5]/div[4]/input")

    continue_button.click()


def find_course(course_name, term):

    wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'desktop_term_select')))
    semester_terms = driver.find_elements_by_class_name(
        "term_radio_item")
    for sem_term_element in semester_terms:
        sem_term = sem_term_element.find_element_by_tag_name(
            "span").get_attribute("innerHTML")
        if(sem_term == term):
            wait.until(
                EC.element_to_be_clickable((By.NAME, 'radterm')))
            radio_btn = sem_term_element.find_element_by_name('radterm')
            radio_btn.click()

    inp = wait.until(EC.element_to_be_clickable((By.ID, 'code_number')))
    inp.send_keys(course_name)
    inp.send_keys(Keys.ENTER)


def course_has_empty_seats():
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'selection_row_radio')))
    lecture_sections = driver.find_elements_by_class_name(
        "selection_row_radio")

    for section in lecture_sections:
        seats_remaining_spans = section.find_elements_by_class_name("seatText")
        if len(seats_remaining_spans) == 0:
            seats_remaining_spans = section.find_elements_by_class_name(
                "fullText")

        for seat_remaining_span in seats_remaining_spans:
            if(seat_remaining_span.get_attribute("innerHTML") == 'Full'):
                return False
    return True


def removeCourse():
    remove_course_btn = driver.find_element_by_xpath(
        "//div[@id='requirements']/div[3]/div[2]/div[1]/a")
    remove_course_btn.click()


open_schedule_builder_page()
find_course("ENCM 467", "2020 Fall")
course_has_empty_seats()
if(course_has_empty_seats()):
    print("Course has seats")
else:
    print("Course is full")
removeCourse()
driver.close()

from AdminLogin import OrangeHRMLogin
import time


if __name__ == "__main__":
    from selenium.common.exceptions import WebDriverException

    hrm = None
    try:
        hrm = OrangeHRMLogin()
        hrm.login(
            url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            username="Admin",
            password="admin123",
        )
        hrm.navigateToMOdule(module='PIM')
        
        employees = [
            {"firstName": "bharatone", "lastName": "last"},
            {"firstName": "bharattwo", "lastName": "last"},
            {"firstName": "bharatthree", "lastName": "last"},
            {"firstName": "bharatfour", "lastName": "last"},
        ]
        hrm.addEmployee(employee_list=employees)
        hrm.logout()

    except WebDriverException as e:
        print(f"[Error] WebDriver error occurred: {e}")
    except Exception as e:
        print(f"[Error] An unexpected error occurred: {e}")
    finally:
        if hrm:
            time.sleep(2)
            hrm.close()
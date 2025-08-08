from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BatchCreation:
    def __init__(self, driver):
        self.driver = driver
       # self.driver.url = "https://preprod.testaonline.com/exam-management/create-batch"

        # Locators->Batch Details
        self.Batch_ID = (By.ID, "outlined-adornment-batchId")
        self.Batch_Size = (By.ID, "outlined-adornment-batchSize")
        self.Scheme = (By.ID, "mui-component-select-schemeId")
        self.Assessment_Start_Date = (By.ID, ":rgf:")
        self.Assessment_End_Date = (By.ID, ":rgh:")
        self.Assessment_Start_Time = (By.ID, ":rfm:")
        self.Assessment_End_Time = (By.ID, ":rfp:")
        self.Batch_Mode = (By.ID, "mui-component-select-batchMode")

        # Proctoring
        self.Enable_Img_proctoring = (
        By.XPATH, "//input[@name='imageProctorStatus' and @type='radio' and @value='true']")
        self.Disable_Img_proctoring = (
        By.XPATH, "//input[@name='imageProctorStatus' and @type='radio' and @value='false']")
        self.Img_proctoring_time = (By.ID, "outlined-adornment-imageProctoringTime")

        self.Enable_Vdo_streaming = (By.XPATH, "//input[@name='videoStreaming' and @type='radio' and @value='true']")
        self.Disable_Vdo_streaming = (By.XPATH, "//input[@name='videoStreaming' and @type='radio' and @value='false']")
        self.Vdo_Duration = (By.ID, "outlined-adornment-videoDuration")
        self.Vdo_Interval = (By.ID, "outlined-adornment-videoInterval")

        self.Enable_Vdo_Proctoring = (
        By.XPATH, "//input[@name='videoScreensharingProctoringStatus' and @type='radio' and @value='true']")
        self.Disable_Vdo_Proctoring = (
        By.XPATH, "//input[@name='videoScreensharingProctoringStatus' and @type='radio' and @value='false']")

        self.Enable_captureImg_status = (
        By.XPATH, "//input[@name='capturingImageStatus' and @type='radio' and @value='true']")
        self.Disable_captureImg_status = (
        By.XPATH, "//input[@name='capturingImageStatus' and @type='radio' and @value='false']")

        self.Enable_face_Recognition = (
        By.XPATH, "//input[@name='faceRecognition' and @type='radio' and @value='true']")
        self.Disable_face_Recognition = (
        By.XPATH, "//input[@name='faceRecognition' and @type='radio' and @value='false']")

        self.Enable_face_Detection = (By.XPATH, "//input[@name='faceDetection' and @type='radio' and @value='true']")
        self.Disable_face_Detection = (By.XPATH, "//input[@name='faceDetection' and @type='radio' and @value='false']")

        self.Enable_wrong_login_Status = (
        By.XPATH, "//input[@name='wrongLoginStatus' and @type='radio' and @value='true']")
        self.Disable_wrong_login_Status = (
        By.XPATH, "//input[@name='wrongLoginStatus' and @type='radio' and @value='false']")
        self.Max_WrongLogin = (By.ID, "outlined-adornment-noOfWrongLogin")

        self.Enable_browser_exit_alert = (
        By.XPATH, "//input[@name='browserExitAlert' and @type='radio' and @value='true']")
        self.Disable_browser_exit_alert = (
        By.XPATH, "//input[@name='browserExitAlert' and @type='radio' and @value='false']")
        self.no_ofSuspeciousActivity = (By.ID, "noOfBrowserExit")

        self.Enable_identity_proof_status = (
        By.XPATH, "//input[@name='identityProofStatus' and @type='radio' and @value='true']")
        self.Disable_identity_proof_status = (
        By.XPATH, "//input[@name='identityProofStatus' and @type='radio' and @value='false']")

        self.Enable_IsAutoLogout = (By.XPATH, "//input[@name='isAutoLogout' and @type='radio' and @value='true']")
        self.Disable_IsAutoLogout = (By.XPATH, "//input[@name='isAutoLogout' and @type='radio' and @value='false']")

        # Question Paper
        self.Job_Role = (By.ID, "asynchronous-demo")
        self.JobRole_Selection = (By.XPATH, "//li[@role='option'][1]")
        self.QP_Code = (By.ID, "mui-component-select-qpCode")

        self.Level = (By.XPATH, "//label[text()='Level']/following-sibling::div")
        self.Level_Selection = (By.XPATH, "//li[@role='option'][1]")

        self.Version = (By.XPATH, "//label[text()='version']/following-sibling::div")
        self.Version_Selection = (By.XPATH, "//li[@role='option'][1]")

        self.Instruction = (By.XPATH, "//label[text()='chooseInstructions']/following-sibling::div")
        self.Instruction_Selection = (By.XPATH, "//li[@role='option'][1]")

        self.Question_Set = (By.ID, "outlined-adornment-questionSet")
        self.Question_type = (By.ID, "mui-component-select-questionType")
        self.Passing_Percentage = (By.ID, "outlined-adornment-passingPercentage")

        self.Section_Theory = (By.XPATH, "//input[@name='sectionName' and @value='theory']")
        self.Section_Viva = (By.XPATH, "//input[@name='sectionName' and @value='viva']")
        self.Section_Practical = (By.XPATH, "//input[@name='sectionName' and @value='practical']")

        self.TheorySection_examDuration = (
        By.XPATH, "//td[text()='Theory']/following-sibling::td[2]//input[@name='examDuration']")

        self.VivaSection_order = (
        By.XPATH, "//td[text()='Viva']/following-sibling::td[1]//div[contains(@class, 'MuiSelect-root')]")
        self.Vivaorder_Selection = (By.XPATH, "//li[text()='2']")
        self.VivaSection_examDuration = (
        By.XPATH, "//td[text()='Viva']/following-sibling::td[2]//input[@name='examDuration']")

        self.PracticalSection_order = (
        By.XPATH, "//td[text()='Practical']/following-sibling::td[1]//div[contains(@class, 'MuiSelect-root')]")
        self.Practicalorder_Selection = (By.XPATH, "//li[text()='3']")
        self.PracticalSection_examDuration = (
        By.XPATH, "//td[text()='Practical']/following-sibling::td[2]//input[@name='examDuration']")

        self.AssessmentStatus_Start = (
        By.XPATH, "//input[@name= 'assesmentStatus' and @type= 'radio' and  @value='true' ]")
        self.AssessmentStatus_Stop = (
        By.XPATH, "//input[@name= 'assesmentStatus' and @type= 'radio' and  @value= 'false' ]")

        self.AssignAssessor_No = (
        By.XPATH, "//input[@name='assignAssessorProctor' and @type= 'radio' and  @value= 'false' ]")
        self.AssignAssessor_yes = (
        By.XPATH, "//input[@name= 'assignAssessorProctor' and @type= 'radio' and  @value= 'true' ]")
        self.AssignAssessor_search = (By.XPATH, "//input[@placeholder='Assessor' and @type= 'text' ]")
        self.AssignAssessor_selection = (By.XPATH, "//li[@role='option'][1]")

        self.FinanceRemark = (By.ID, "outlined-adornment-financeRemarks")
        self.submitBtn = (By.XPATH, "//button[normalize-space(text()) = 'Submit']")
        self.cancelLink = (By.XPATH, "//button[normalize-space(text()) = 'Cancel']")


#Method


    def open_page(self, driver):
        self.driver.get(self.driver.url)

    def enter_batch_details(self, Batch_ID, Batch_Size):
        self.driver.find_element(*self.Batch_ID).send_keys(Batch_ID)
        self.driver.find_element(*self.Batch_Size).send_keys(Batch_Size)
        self.driver.find_element(*self.Scheme).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@role='option'][1]"))
        ).click()

    def set_assessment_dates(self, driver, start_date, end_date):
        self.driver.find_element(self.driver.Assessment_Start_Date).send_keys("start_date")
        self.driver.find_element(self.driver.Assessment_End_Date).send_keys(end_date)



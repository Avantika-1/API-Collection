import allure
import pytest
import requests

@pytest.mark.sanity
@allure.description("Positive scenario: Create batch")
def test_create_batch():
    base_url = "https://api.testaonline.com"
    endpoint = "/api/createbatch"
    url = base_url + endpoint

    headers = {
        "x-auth-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFiaGlqZWV0QHJhZGlhbnRpbmZvbmV0LmNvbSIsImlwIjoiMTQuOTkuMTU1LjY2IiwiaWF0IjoxNzUxNTQ0NzQxLCJleHAiOjE3NTE2MzExNDF9.BNOXH4sDEiWGZojhebJt69xBmXHYLItKW5Jp9mBf33o",
        "content-type": "application/json"
    }

    payload = {
        "batchSize":"2394","batchId":"testbatch","startDate":"03/07/2025","endDate":"31/07/2025","startTime":"12:00AM","endTime":"11:54PM","schemeId":"673ae2a21d9f795a1f756974","subSchemeId":"","batchMode":"online",
        "proctoring":{"imageProctor":{"imageProctorStatus":True,"imageProctoringTime":1},"videoStream":{"videoStreaming":True,"videoDuration":5,"videoInterval":1},"wrongLogin":{"wrongLoginStatus":True,"noOfWrongLogin":3},"browserExit":{"browserExitAlert":True,"noOfBrowserExit":7},"isAutoLogout":False,"faceRecognition":False,"faceDetection":False,"videoScreensharingProctoringStatus":True,"capturingImageStatus":True,"identityProofStatus":True},
        "questionPaper":{"suffleQuestion":True,"optionRandom":False,"markForReview":True,"questionNavigation":True,"paginationStatus":True,"examLanguageConduct":False,"primaryLanguage":"english","questionSet":"1","assesmentStatus":True,"questionType":"objective",
        "sectionTable":[{"sectionName":"theory","sectionOrder":1,"examDuration":"20","isSelected":True},{"sectionName":"viva","sectionOrder":2,"examDuration":"20","isSelected":False},{"sectionName":"practical","sectionOrder":3,"examDuration":"20","isSelected":True}],
        "passingPercentage":"30","chooseInstructions":"67f78f52e34f8e11692ce40e","level":"5","qpCode":"673d84a1567847b4f2041153","version":"3","isMultiJobRole":False},"jobRole":"673d84a1567847b4f2041153","assignAssessorProctor":True,"accessorId":"67483e240003919c6dbf5e1b","financeRemarks":"test"}
    response = requests.post(url=url, headers=headers, json=payload)

    print("Response Text:", response.text)
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
